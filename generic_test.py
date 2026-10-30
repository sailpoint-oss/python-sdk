"""Offline tests for the generic API client.

The requests go to a local HTTP server, so these tests need no tenant. They
require the SDK to be built first:
    node sdk-resources/build-versioned-sdk.js --generic-only
"""

import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit

from sailpoint import ApiClient, GenericApi
from sailpoint.configuration import Configuration, ConfigurationParams


class _CapturingHandler(BaseHTTPRequestHandler):
    """Records each request and answers with the server's canned JSON body."""

    def _handle(self):
        length = int(self.headers.get("Content-Length") or 0)
        self.server.captured = {
            "method": self.command,
            "url": urlsplit(self.path),
            "content_type": self.headers.get("Content-Type"),
            "auth": self.headers.get("Authorization"),
            "body": self.rfile.read(length).decode() if length else "",
        }
        payload = self.server.response.encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_GET = do_POST = do_PUT = do_PATCH = do_DELETE = _handle

    def log_message(self, format, *args):
        pass


class TestGenericApi(unittest.TestCase):

    def setUp(self):
        self.server = HTTPServer(("127.0.0.1", 0), _CapturingHandler)
        self.server.response = "{}"
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

        params = ConfigurationParams()
        params.base_url = f"http://127.0.0.1:{self.server.server_port}"
        params.access_token = "token-1"
        self.api = GenericApi(ApiClient(Configuration(params)))

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def test_keeps_slashes_and_adds_no_version(self):
        self.server.response = '[{"id": "1"}]'

        result = self.api.generic_get(
            path="/entitlements/v1/identities/2c91808a/entitlements", limit=10, filters='name eq "x"'
        )

        captured = self.server.captured
        self.assertEqual(captured["url"].path, "/entitlements/v1/identities/2c91808a/entitlements")
        query = parse_qs(captured["url"].query)
        self.assertEqual(query["limit"], ["10"])
        self.assertEqual(query["filters"], ['name eq "x"'])
        self.assertEqual(captured["auth"], "Bearer token-1")
        self.assertEqual(result, [{"id": "1"}])

    def test_encodes_segments_and_keeps_query_from_path(self):
        self.api.generic_get(path="accounts/v1/a b?detailLevel=SLIM", limit=5)

        captured = self.server.captured
        self.assertEqual(captured["url"].path, "/accounts/v1/a%20b")
        query = parse_qs(captured["url"].query)
        self.assertEqual(query["detailLevel"], ["SLIM"])
        self.assertEqual(query["limit"], ["5"])

    def test_patch_sends_json_patch_list(self):
        patch = [{"op": "replace", "path": "/description", "value": "New"}]

        self.api.generic_patch(path="transforms/v1/1234", request_body=patch)

        captured = self.server.captured
        self.assertEqual(captured["method"], "PATCH")
        self.assertEqual(captured["content_type"], "application/json-patch+json")
        self.assertEqual(json.loads(captured["body"]), patch)

    def test_post_sends_json_body_to_v2_path(self):
        self.server.response = '{"id": "1"}'

        result = self.api.generic_post(path="sources/v2/2c91808a/provisioning-policies", request_body={"name": "Test", "type": "lower"})

        captured = self.server.captured
        self.assertEqual(captured["method"], "POST")
        self.assertEqual(captured["url"].path, "/sources/v2/2c91808a/provisioning-policies")
        self.assertEqual(json.loads(captured["body"]), {"name": "Test", "type": "lower"})
        self.assertEqual(result, {"id": "1"})


if __name__ == "__main__":
    unittest.main()
