import copy
import http.client as httplib
import json
import logging
import multiprocessing
import os
import ssl
import sys

import urllib3

SUPPORTED_SOCKS_PROXIES = {"socks5", "socks5h", "socks4", "socks4a"}

def is_socks_proxy_url(url):
    if url is None:
        return False
    split_section = url.split("://")
    if len(split_section) < 2:
        return False
    else:
        return split_section[0].lower() in SUPPORTED_SOCKS_PROXIES



class ConfigurationParams:
    base_url = None
    client_id = None
    client_secret = None
    token_url = None
    access_token = None
    ssl_ca_cert = None
    proxy = None
    proxy_headers = None
    verify_ssl = True

class Configuration:
    def __init__(self, configurationParams: ConfigurationParams = None) -> None:
        defaultConfiguration = self.get_configuration_params()

        self.base_url = configurationParams.base_url if configurationParams and configurationParams.base_url else defaultConfiguration.base_url
        self.client_id = configurationParams.client_id if configurationParams and configurationParams.client_id else defaultConfiguration.client_id
        self.client_secret = configurationParams.client_secret if configurationParams and configurationParams.client_secret else defaultConfiguration.client_secret
        self.token_url = str(configurationParams.base_url) + "/oauth/token" if configurationParams and configurationParams.base_url else defaultConfiguration.token_url
        self.access_token = configurationParams.access_token if configurationParams and configurationParams.access_token else defaultConfiguration.access_token
        self.proxy = configurationParams.proxy if configurationParams and configurationParams.proxy else None
        self.proxy_headers = configurationParams.proxy_headers if configurationParams and configurationParams.proxy_headers else None
        self.verify_ssl = configurationParams.verify_ssl if configurationParams and configurationParams.verify_ssl else True

        url = f"{self.token_url}"
        if self.access_token == None:
            self.access_token = self.get_access_token(url, self.client_id, self.client_secret, self.proxy, self.proxy_headers, self.verify_ssl)

        self.experimental = False
        self.suppress_experimental_warnings = False

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
        self.ssl_ca_cert = defaultConfiguration.ssl_ca_cert
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

        return ConfigurationParams()

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
    def get_access_token(self, url: str, client_id: str, client_secret: str, proxy: str, proxy_headers: dict, verify_ssl: bool) -> str:

        http = urllib3.PoolManager()
        pool_args = {}

        if verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        if proxy:
            if is_socks_proxy_url(proxy):
                from urllib3.contrib.socks import SOCKSProxyManager
                pool_args["proxy_url"] = proxy
                pool_args["headers"] = proxy_headers
                pool_args["cert_reqs"] = cert_reqs
                http = SOCKSProxyManager(**pool_args)
            else:
                pool_args["proxy_url"] = proxy
                pool_args["proxy_headers"] = proxy_headers
                pool_args["cert_reqs"] = cert_reqs
                http = urllib3.ProxyManager(**pool_args)
        else:
            http = urllib3.PoolManager(**pool_args)

        try:
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
