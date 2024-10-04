import json
import os
import copy
import logging
import multiprocessing
import sys
import urllib3

import http.client as httplib


class ConfigurationParams:
    base_url = None
    client_id = None
    client_secret = None
    token_url = None
    access_token = None
    ssl_ca_cert = None


class Configuration:
    def __init__(self, configurationParams: ConfigurationParams = None) -> None:
        if configurationParams == None:
            configurationParams = self.get_configuration_params()

            self.access_token = configurationParams.access_token
            self.base_url = configurationParams.base_url
            self.client_id = configurationParams.client_id
            self.client_secret = configurationParams.client_secret
            self.token_url = configurationParams.token_url

        else:
            self.access_token = configurationParams.access_token
            self.base_url = configurationParams.base_url
            self.client_id = configurationParams.client_id
            self.client_secret = configurationParams.client_secret
            self.token_url = str(configurationParams.base_url) + "/oauth/token"


        url = f"{self.token_url}"
        if self.access_token == None:
            self.access_token = self.get_access_token(url, self.client_id, self.client_secret)



        self.experimental = False

        self.temp_folder_path = None
        """Temp file folder for downloading files
        """

        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """

        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("v3")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = "%(asctime)s %(levelname)s %(message)s"
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = configurationParams.ssl_ca_cert
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ""
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        self.socket_options = None
        """Options to pass down to the underlying urllib3 socket
        """

        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        """datetime format
        """

        self.date_format = "%Y-%m-%d"
        """date format
        """

    @classmethod
    def get_configuration_params(self):
        envConfiguration = self.get_environment_params()
        if envConfiguration.base_url:
            return envConfiguration

        localConfiguration = self.get_local_params()
        if localConfiguration.base_url:
            return localConfiguration

        return {}

    @classmethod
    def get_environment_params(self) -> ConfigurationParams:
        config = ConfigurationParams()

        config.base_url = (
            os.environ.get("SAIL_BASE_URL") if os.environ.get("SAIL_BASE_URL") else None
        )
        config.client_id = (
            os.environ.get("SAIL_CLIENT_ID")
            if os.environ.get("SAIL_CLIENT_ID")
            else None
        )
        config.client_secret = (
            os.environ.get("SAIL_CLIENT_SECRET")
            if os.environ.get("SAIL_CLIENT_SECRET")
            else None
        )
        config.token_url = str(config.base_url) + "/oauth/token"

        return config

    @classmethod
    def get_local_params(self) -> ConfigurationParams:
        config = ConfigurationParams()
        if os.path.exists("./config.json"):
            ("File is present")
            with open("./config.json") as file:
                data = json.load(file)
                config.base_url = data["BaseURL"]
                config.client_id = data["ClientId"]
                config.client_secret = data["ClientSecret"]
                config.token_url = config.base_url + "/oauth/token"
                return config

    @classmethod
    def get_access_token(self, url: str, client_id: str, client_secret: str) -> str:
        try:
            http = urllib3.PoolManager()
            response = http.request_encode_body("POST", url, encode_multipart=False, fields={"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret})
            data = json.loads(response.data)
            if response.status == 200:
                return data["access_token"]
            elif response.status == 401:
                raise Exception("Unauthorized when retrieving access token.")
            else:
                raise Exception(
                    "There was an error while trying to fetch access token: "
                    + str(response.data)
                )
        except Exception as e:
            print("Unable to fetch access token. %s" % e)

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.access_token is not None:
            auth["userAuth"] = {
                "type": "oauth2",
                "in": "header",
                "key": "Authorization",
                "value": "Bearer " + self.access_token,
            }
        if self.access_token is not None:
            auth["userAuth"] = {
                "type": "oauth2",
                "in": "header",
                "key": "Authorization",
                "value": "Bearer " + self.access_token,
            }
        if self.access_token is not None:
            auth["applicationAuth"] = {
                "type": "oauth2",
                "in": "header",
                "key": "Authorization",
                "value": "Bearer " + self.access_token,
            }
        return auth
