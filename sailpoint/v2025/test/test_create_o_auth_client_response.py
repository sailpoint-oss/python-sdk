# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.create_o_auth_client_response import CreateOAuthClientResponse

class TestCreateOAuthClientResponse(unittest.TestCase):
    """CreateOAuthClientResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOAuthClientResponse:
        """Test CreateOAuthClientResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOAuthClientResponse`
        """
        model = CreateOAuthClientResponse()
        if include_optional:
            return CreateOAuthClientResponse(
                id = '2c9180835d2e5168015d32f890ca1581',
                secret = '5c32dd9b21adb51c77794d46e71de117a1d0ddb36a7ff941fa28014ab7de2cf3',
                business_name = 'Acme-Solar',
                homepage_url = 'http://localhost:12345',
                name = 'Demo API Client',
                description = 'An API client used for the authorization_code, refresh_token, and client_credentials flows',
                access_token_validity_seconds = 750,
                refresh_token_validity_seconds = 86400,
                redirect_uris = [http://localhost:12345],
                grant_types = [AUTHORIZATION_CODE, CLIENT_CREDENTIALS, REFRESH_TOKEN],
                access_type = 'OFFLINE',
                type = 'CONFIDENTIAL',
                internal = False,
                enabled = True,
                strong_auth_supported = False,
                claims_supported = False,
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-06-25T20:22:28.104Z',
                scope = [demo:api-client-scope:first, demo:api-client-scope:second]
            )
        else:
            return CreateOAuthClientResponse(
                id = '2c9180835d2e5168015d32f890ca1581',
                secret = '5c32dd9b21adb51c77794d46e71de117a1d0ddb36a7ff941fa28014ab7de2cf3',
                business_name = 'Acme-Solar',
                homepage_url = 'http://localhost:12345',
                name = 'Demo API Client',
                description = 'An API client used for the authorization_code, refresh_token, and client_credentials flows',
                access_token_validity_seconds = 750,
                refresh_token_validity_seconds = 86400,
                redirect_uris = [http://localhost:12345],
                grant_types = [AUTHORIZATION_CODE, CLIENT_CREDENTIALS, REFRESH_TOKEN],
                access_type = 'OFFLINE',
                type = 'CONFIDENTIAL',
                internal = False,
                enabled = True,
                strong_auth_supported = False,
                claims_supported = False,
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-06-25T20:22:28.104Z',
                scope = [demo:api-client-scope:first, demo:api-client-scope:second],
        )
        """

    def testCreateOAuthClientResponse(self):
        """Test CreateOAuthClientResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
