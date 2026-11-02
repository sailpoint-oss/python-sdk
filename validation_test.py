from typing import Any
import unittest


# ---------------------------------------------------------------------------
# V1 partition imports
# ---------------------------------------------------------------------------
# These imports require the versioned SDK to be built first:
#   node sdk-resources/build-versioned-sdk.js <path-to-apis>
#
# Each partition lives under sailpoint/{partition}_v1/.

try:
    from sailpoint import (
        ApiClient,
        AccountsApi, SearchApi, TransformsApi,
        ConnectorsApi, SourcesApi, IdentityProfilesApi,
        IdentitiesApi, TaskManagementApi, GenericApi,
    )
    HAS_V1 = True
except ImportError:
    HAS_V1 = False

from sailpoint.configuration import Configuration, ConfigurationParams
from sailpoint.paginator import Paginator


class TestPythonSDKV1(unittest.TestCase):
    """Tests using the new per-partition V1 packages."""

    @classmethod
    def setUpClass(cls):
        if not HAS_V1:
            raise unittest.SkipTest(
                "V1 partition packages not built yet. "
                "Run: node sdk-resources/build-versioned-sdk.js <path-to-apis>"
            )

    def setUp(self):
        self.configuration = Configuration()
        self.api_client = ApiClient(self.configuration)

    def _accounts_client(self):
        return self.api_client

    def _search_client(self):
        return self.api_client

    def _transforms_client(self):
        return self.api_client

    def test_manual_configuration(self):
        params = ConfigurationParams()
        params.base_url = "https://localhost:8080"
        params.client_id = "client_id"
        params.client_secret = "client_secret"
        cfg = Configuration(params)

        self.assertEqual(cfg.base_url, "https://localhost:8080")
        self.assertEqual(cfg.client_id, "client_id")
        self.assertEqual(cfg.client_secret, "client_secret")

    def test_accounts_v1(self):
        result = AccountsApi(self._accounts_client()).list_accounts_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_list_transforms_v1(self):
        result = TransformsApi(self._transforms_client()).list_transforms_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_search_pagination_v1(self):
        from sailpoint.search.models.search import Search
        search = Search()
        search.indices = ['identities']
        search.query = {'query': '*'}
        search.sort = ['-name']

        results = Paginator.paginate_search_with_http_info(
            SearchApi(self.api_client), search, 10, 100
        )
        self.assertIsNotNone(results)
        self.assertEqual(100, len(results.data))
        self.assertEqual(200, results.status_code)

    def test_paginate_stream_search_v1(self):
        from sailpoint.search.models.search import Search
        search = Search()
        search.indices = ['identities']
        search.query = {'query': '*'}
        search.sort = ['-name']

        items = list(Paginator.paginate_stream_search(
            SearchApi(self.api_client), search, 10, 100
        ))
        self.assertEqual(100, len(items))

    def test_pagination_v1(self):
        accounts = Paginator.paginate(
            AccountsApi(self.api_client).list_accounts_v1_with_http_info, 100, limit=10
        )
        self.assertIsNotNone(accounts.data)
        self.assertEqual(100, len(accounts.data))
        self.assertEqual(200, accounts.status_code)

    def test_paginate_stream_v1(self):
        items = list(Paginator.paginate_stream(
            AccountsApi(self.api_client).list_accounts_v1_with_http_info, 100, limit=10
        ))
        self.assertEqual(100, len(items))

    def test_paginate_stream_consumed_incrementally_v1(self):
        stream = Paginator.paginate_stream(
            AccountsApi(self.api_client).list_accounts_v1_with_http_info, 100, limit=2
        )
        first_three = []
        for i, item in enumerate(stream):
            first_three.append(item)
            if i >= 2:
                break
        self.assertGreaterEqual(len(first_three), 1)
        self.assertLessEqual(len(first_three), 3)

    def test_paginate_stream_with_model_v1(self):
        from sailpoint.accounts.models.account import Account
        stream = Paginator.paginate_stream(
            AccountsApi(self.api_client).list_accounts_v1_with_http_info,
            10, limit=5, model=Account
        )
        for item in stream:
            self.assertIsInstance(item, Account)
            break

    def test_paginate_stream_with_http_info_v1(self):
        items = []
        for item, response in Paginator.paginate_stream_with_http_info(
            AccountsApi(self.api_client).list_accounts_v1_with_http_info, 100, limit=10
        ):
            self.assertEqual(200, response.status_code)
            items.append(item)
        self.assertEqual(100, len(items))

    def test_paginate_stream_search_with_http_info_v1(self):
        from sailpoint.search.models.search import Search
        search = Search()
        search.indices = ['identities']
        search.query = {'query': '*'}
        search.sort = ['-name']

        items = []
        for item, response in Paginator.paginate_stream_search_with_http_info(
            SearchApi(self.api_client), search, 10, 100
        ):
            self.assertEqual(200, response.status_code)
            items.append(item)
        self.assertEqual(100, len(items))

    def test_list_connectors_v1(self):
        result = ConnectorsApi(self.api_client).get_connector_list_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_list_sources_v1(self):
        result = SourcesApi(self.api_client).list_sources_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    # The generic client calls any versioned endpoint by path, with the same
    # configuration and token as the resource clients.
    def test_generic_get_v1(self):
        result = GenericApi(self.api_client).generic_get_with_http_info(path="sources/v1", limit=10)
        self.assertEqual(200, result.status_code)
        self.assertIsInstance(result.data, list)
        self.assertLessEqual(len(result.data), 10)

    # access-request-config/v2 is experimental, so this also covers the
    # experimental opt-in.
    def test_generic_get_v2(self):
        self.configuration.experimental = True
        result = GenericApi(self.api_client).generic_get_with_http_info(
            path="access-request-config/v2", x_sail_point_experimental="true"
        )
        self.assertEqual(200, result.status_code)
        self.assertIsInstance(result.data, dict)

    def test_list_identity_profiles_v1(self):
        result = Paginator.paginate(
            IdentityProfilesApi(self.api_client).list_identity_profiles_v1_with_http_info,
            2, limit=1
        )
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)
        self.assertEqual(2, len(result.data))

    def test_list_identities_v1(self):
        result = IdentitiesApi(self.api_client).list_identities_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_task_management_v1(self):
        result = TaskManagementApi(self.api_client).get_task_status_list_v1_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_sailpoint_namespace(self):
        """SailPoint namespace exposes resource-named API classes (no version in name)."""
        from sailpoint import SailPoint, AccountsApi, TransformsApi
        self.assertTrue(hasattr(SailPoint, "AccountsApi"))
        self.assertTrue(hasattr(SailPoint, "TransformsApi"))
        self.assertIsNotNone(AccountsApi)
        self.assertIsNotNone(TransformsApi)
        # Versioned classes are still importable directly from the partition sub-package
        from sailpoint.accounts import AccountsApi as _AccountsApi
        from sailpoint.transforms import TransformsApi as _TransformsApi
        self.assertIsNotNone(_AccountsApi)
        self.assertIsNotNone(_TransformsApi)


class TestLenientEnumsV1(unittest.TestCase):
    """
    Validate that enum refs use Union[EnumType, str] so unknown values from the API
    are accepted as plain strings (lenient enum validation).
    """

    @classmethod
    def setUpClass(cls):
        if not HAS_V1:
            raise unittest.SkipTest(
                "V1 partition packages not built yet. "
                "Run: node sdk-resources/build-versioned-sdk.js <path-to-apis>"
            )

    def test_requested_item_status_accepts_known_state_enum(self):
        """Known state value is coerced to the RequestedItemStatusRequestState enum member."""
        from sailpoint.access_requests.models.requested_item_status import RequestedItemStatus
        from sailpoint.access_requests.models.requested_item_status_request_state import RequestedItemStatusRequestState

        obj = RequestedItemStatus.model_validate({"state": "EXECUTING"})
        self.assertIsNotNone(obj.state)
        self.assertEqual(obj.state, RequestedItemStatusRequestState.EXECUTING)

    def test_requested_item_status_accepts_unknown_state_as_str(self):
        """Unknown state value is accepted as plain str (lenient enum)."""
        from sailpoint.access_requests.models.requested_item_status import RequestedItemStatus

        unknown_state = "FUTURE_STATE_NOT_IN_SPEC"
        obj = RequestedItemStatus.model_validate({"state": unknown_state})
        self.assertIsNotNone(obj.state)
        self.assertEqual(obj.state, unknown_state)
        self.assertIsInstance(obj.state, str)

    def test_requested_item_status_accepts_known_request_type_enum(self):
        """Known request_type value is coerced to AccessRequestType enum member."""
        from sailpoint.access_requests.models.requested_item_status import RequestedItemStatus
        from sailpoint.access_requests.models.access_request_type import AccessRequestType

        obj = RequestedItemStatus.model_validate({"requestType": "GRANT_ACCESS"})
        self.assertIsNotNone(obj.request_type)
        self.assertEqual(obj.request_type, AccessRequestType.GRANT_ACCESS)

    def test_requested_item_status_accepts_unknown_request_type_as_str(self):
        """Unknown request_type value is accepted as plain str (lenient enum)."""
        from sailpoint.access_requests.models.requested_item_status import RequestedItemStatus

        unknown_type = "FUTURE_REQUEST_TYPE"
        obj = RequestedItemStatus.model_validate({"requestType": unknown_type})
        self.assertIsNotNone(obj.request_type)
        self.assertEqual(obj.request_type, unknown_type)
        self.assertIsInstance(obj.request_type, str)

    def test_requested_item_status_unknown_state_round_trips_in_dict(self):
        """Unknown state serializes and deserializes correctly (e.g. for API responses)."""
        from sailpoint.access_requests.models.requested_item_status import RequestedItemStatus

        unknown_state = "PENDING_NEW_BACKEND"
        obj = RequestedItemStatus.model_validate({"state": unknown_state})
        d = obj.model_dump(by_alias=True)
        self.assertIn("state", d)
        self.assertEqual(d["state"], unknown_state)
        obj2 = RequestedItemStatus.model_validate(d)
        self.assertEqual(obj2.state, unknown_state)


class TestNermSDK(unittest.TestCase):
    """Tests for the NERM SDK (base and v2025)."""

    @classmethod
    def setUpClass(cls):
        cfg = Configuration()
        if not cfg.nerm_base_url:
            raise unittest.SkipTest(
                "NERM not configured. Set NermBaseUrl in config.json or SAIL_NERM_BASE_URL env var."
            )

    def setUp(self):
        self.configuration = Configuration()
        from sailpoint.nerm.api_client import ApiClient as NermApiClient
        from sailpoint.nerm.v2025.api_client import ApiClient as NermV2025ApiClient
        self.nerm_api_client = NermApiClient(self.configuration)
        self.nerm_v2025_api_client = NermV2025ApiClient(self.configuration)

    def test_nerm_list_users(self):
        from sailpoint.nerm.api.users_api import UsersApi
        result = UsersApi(self.nerm_api_client).get_users_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)

    def test_nerm_v2025_list_delegations(self):
        from sailpoint.nerm.v2025.api.delegations_api import DelegationsApi
        result = DelegationsApi(self.nerm_v2025_api_client).delegations_get_with_http_info()
        self.assertIsNotNone(result.data)
        self.assertEqual(200, result.status_code)


class TestLazyImports(unittest.TestCase):
    """
    sailpoint/__init__.py resolves API classes lazily (PEP 562), so importing the
    package must not import any partition package. These tests need no tenant.
    """

    # Shared, non-partition modules that `import sailpoint` is allowed to load
    ROOT_MODULES = {"api_client", "api_response", "configuration", "exceptions", "paginator", "rest"}

    @classmethod
    def setUpClass(cls):
        if not HAS_V1:
            raise unittest.SkipTest(
                "V1 partition packages not built yet. "
                "Run: node sdk-resources/build-versioned-sdk.js <path-to-apis>"
            )

    def _loaded_partitions(self, code):
        """Run `code` in a fresh interpreter and return the sailpoint partitions it loaded."""
        import os
        import subprocess
        import sys
        script = (
            code + "\n"
            "import sys\n"
            "print(','.join(sorted({m.split('.')[1] for m in sys.modules if m.startswith('sailpoint.')})))\n"
        )
        out = subprocess.run(
            [sys.executable, "-c", script],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True, text=True, check=True,
        ).stdout.strip().splitlines()[-1]
        return set(filter(None, out.split(","))) - self.ROOT_MODULES

    def test_import_sailpoint_loads_no_partitions(self):
        self.assertEqual(set(), self._loaded_partitions("import sailpoint"))

    def test_import_one_api_loads_only_its_partition(self):
        self.assertEqual({"search"}, self._loaded_partitions("from sailpoint import SearchApi"))

    def test_namespace_access_loads_only_its_partition(self):
        self.assertEqual(
            {"sources"},
            self._loaded_partitions("from sailpoint import SailPoint\nSailPoint.SourcesApi"),
        )

    def test_flat_imports(self):
        from sailpoint import SourcesApi, ApiClient, Configuration, ConfigurationParams, Paginator
        from sailpoint.sources import SourcesApi as PartitionSourcesApi
        from sailpoint.sources.api.sources_api import SourcesApi as ModuleSourcesApi
        self.assertIs(SourcesApi, PartitionSourcesApi)
        self.assertIs(SourcesApi, ModuleSourcesApi)
        self.assertIsNotNone(ApiClient)
        self.assertIsNotNone(Configuration)
        self.assertIsNotNone(ConfigurationParams)
        self.assertIsNotNone(Paginator)

    def test_namespace_matches_flat_exports(self):
        import sailpoint
        from sailpoint import SailPoint
        self.assertIs(SailPoint.SourcesApi, sailpoint.SourcesApi)
        self.assertIs(SailPoint.RolesApi, sailpoint.RolesApi)
        self.assertIn("SourcesApi", dir(SailPoint))

    def test_combined_classes_expose_both_partitions(self):
        import sailpoint
        from sailpoint import RolesApi, WorkflowsApi
        from sailpoint.roles.api.roles_api import RolesApi as IscRolesApi
        from sailpoint.nerm.api.roles_api import RolesApi as NermRolesApi
        from sailpoint.workflows.api.workflows_api import WorkflowsApi as IscWorkflowsApi
        from sailpoint.nerm.api.workflows_api import WorkflowsApi as NermWorkflowsApi
        self.assertTrue(issubclass(RolesApi, IscRolesApi))
        self.assertTrue(issubclass(RolesApi, NermRolesApi))
        self.assertTrue(issubclass(WorkflowsApi, IscWorkflowsApi))
        self.assertTrue(issubclass(WorkflowsApi, NermWorkflowsApi))
        # Built once and cached, so every access returns the same class
        self.assertIs(RolesApi, sailpoint.RolesApi)
        self.assertIs(WorkflowsApi, sailpoint.WorkflowsApi)

    def test_every_export_resolves(self):
        import sailpoint
        for name in sailpoint.__all__:
            with self.subTest(name=name):
                self.assertIsNotNone(getattr(sailpoint, name))
        self.assertTrue(set(sailpoint.__all__) <= set(dir(sailpoint)))

    def test_star_import(self):
        namespace = {}
        exec("from sailpoint import *", namespace)
        self.assertIn("SourcesApi", namespace)
        self.assertIn("ApiClient", namespace)
        self.assertIn("SailPoint", namespace)

    def test_unknown_names_raise_attribute_error(self):
        import sailpoint
        from sailpoint import SailPoint
        with self.assertRaises(AttributeError):
            sailpoint.NotARealApi
        with self.assertRaises(AttributeError):
            SailPoint.NotARealApi
        with self.assertRaises(ImportError):
            from sailpoint import NotARealApi  # noqa: F401


if __name__ == '__main__':
    unittest.main()
