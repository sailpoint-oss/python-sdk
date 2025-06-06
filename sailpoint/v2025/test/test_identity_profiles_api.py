# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.api.identity_profiles_api import IdentityProfilesApi


class TestIdentityProfilesApi(unittest.TestCase):
    """IdentityProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentityProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_create_identity_profile(self) -> None:
        """Test case for create_identity_profile

        Create identity profile
        """
        pass

    def test_delete_identity_profile(self) -> None:
        """Test case for delete_identity_profile

        Delete identity profile
        """
        pass

    def test_delete_identity_profiles(self) -> None:
        """Test case for delete_identity_profiles

        Delete identity profiles
        """
        pass

    def test_export_identity_profiles(self) -> None:
        """Test case for export_identity_profiles

        Export identity profiles
        """
        pass

    def test_generate_identity_preview(self) -> None:
        """Test case for generate_identity_preview

        Generate identity profile preview
        """
        pass

    def test_get_default_identity_attribute_config(self) -> None:
        """Test case for get_default_identity_attribute_config

        Get default identity attribute config
        """
        pass

    def test_get_identity_profile(self) -> None:
        """Test case for get_identity_profile

        Get identity profile
        """
        pass

    def test_import_identity_profiles(self) -> None:
        """Test case for import_identity_profiles

        Import identity profiles
        """
        pass

    def test_list_identity_profiles(self) -> None:
        """Test case for list_identity_profiles

        List identity profiles
        """
        pass

    def test_sync_identity_profile(self) -> None:
        """Test case for sync_identity_profile

        Process identities under profile
        """
        pass

    def test_update_identity_profile(self) -> None:
        """Test case for update_identity_profile

        Update identity profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
