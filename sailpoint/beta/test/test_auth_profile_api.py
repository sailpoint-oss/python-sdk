# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.auth_profile_api import AuthProfileApi


class TestAuthProfileApi(unittest.TestCase):
    """AuthProfileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthProfileApi()

    def tearDown(self) -> None:
        pass

    def test_create_profile_config(self) -> None:
        """Test case for create_profile_config

        Create Auth Profile.
        """
        pass

    def test_delete_profile_config(self) -> None:
        """Test case for delete_profile_config

        Delete the specified Auth Profile
        """
        pass

    def test_get_profile_config(self) -> None:
        """Test case for get_profile_config

        Get Auth Profile.
        """
        pass

    def test_get_profile_config_list(self) -> None:
        """Test case for get_profile_config_list

        Get list of Auth Profiles.
        """
        pass

    def test_patch_profile_config(self) -> None:
        """Test case for patch_profile_config

        Patch a specified Auth Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()