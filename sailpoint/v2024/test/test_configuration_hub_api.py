# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.api.configuration_hub_api import ConfigurationHubApi


class TestConfigurationHubApi(unittest.TestCase):
    """ConfigurationHubApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConfigurationHubApi()

    def tearDown(self) -> None:
        pass

    def test_create_object_mapping(self) -> None:
        """Test case for create_object_mapping

        Creates an object mapping
        """
        pass

    def test_create_object_mappings(self) -> None:
        """Test case for create_object_mappings

        Bulk creates object mappings
        """
        pass

    def test_delete_object_mapping(self) -> None:
        """Test case for delete_object_mapping

        Deletes an object mapping
        """
        pass

    def test_delete_uploaded_backup(self) -> None:
        """Test case for delete_uploaded_backup

        Deletes an uploaded backup file
        """
        pass

    def test_get_object_mappings(self) -> None:
        """Test case for get_object_mappings

        Gets list of object mappings
        """
        pass

    def test_get_uploaded_backup(self) -> None:
        """Test case for get_uploaded_backup

        Get an uploaded backup's information
        """
        pass

    def test_get_uploaded_backups(self) -> None:
        """Test case for get_uploaded_backups

        Gets list of Uploaded backups
        """
        pass

    def test_import_uploaded_backup(self) -> None:
        """Test case for import_uploaded_backup

        Uploads a backup file
        """
        pass

    def test_update_object_mappings(self) -> None:
        """Test case for update_object_mappings

        Bulk updates object mappings
        """
        pass


if __name__ == '__main__':
    unittest.main()
