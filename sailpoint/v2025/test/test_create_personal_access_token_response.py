# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.create_personal_access_token_response import CreatePersonalAccessTokenResponse

class TestCreatePersonalAccessTokenResponse(unittest.TestCase):
    """CreatePersonalAccessTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePersonalAccessTokenResponse:
        """Test CreatePersonalAccessTokenResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePersonalAccessTokenResponse`
        """
        model = CreatePersonalAccessTokenResponse()
        if include_optional:
            return CreatePersonalAccessTokenResponse(
                id = '86f1dc6fe8f54414950454cbb11278fa',
                secret = '1d1bef2b9f426383447f64f69349fc7cac176042578d205c256ba3f37c59adb9',
                scope = [demo:personal-access-token-scope:first, demo:personal-access-token-scope:second],
                name = 'NodeJS Integration',
                owner = sailpoint.v2025.models.pat_owner.PatOwner(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                created = '2017-07-11T18:45:37.098Z',
                access_token_validity_seconds = 36900
            )
        else:
            return CreatePersonalAccessTokenResponse(
                id = '86f1dc6fe8f54414950454cbb11278fa',
                secret = '1d1bef2b9f426383447f64f69349fc7cac176042578d205c256ba3f37c59adb9',
                scope = [demo:personal-access-token-scope:first, demo:personal-access-token-scope:second],
                name = 'NodeJS Integration',
                owner = sailpoint.v2025.models.pat_owner.PatOwner(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                created = '2017-07-11T18:45:37.098Z',
                access_token_validity_seconds = 36900,
        )
        """

    def testCreatePersonalAccessTokenResponse(self):
        """Test CreatePersonalAccessTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
