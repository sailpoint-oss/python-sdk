# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.auth_profile import AuthProfile

class TestAuthProfile(unittest.TestCase):
    """AuthProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthProfile:
        """Test AuthProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthProfile`
        """
        model = AuthProfile()
        if include_optional:
            return AuthProfile(
                name = 'EndToEnd-Profile',
                off_network = True,
                untrusted_geography = True,
                application_id = '2c91808458ae7a4f0158b1bbf8af0628',
                application_name = 'EndToEnd-Source',
                type = 'PTA',
                strong_auth_login = True
            )
        else:
            return AuthProfile(
        )
        """

    def testAuthProfile(self):
        """Test AuthProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
