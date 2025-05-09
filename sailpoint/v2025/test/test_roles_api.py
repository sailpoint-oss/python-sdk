# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.api.roles_api import RolesApi


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RolesApi()

    def tearDown(self) -> None:
        pass

    def test_create_role(self) -> None:
        """Test case for create_role

        Create a Role
        """
        pass

    def test_delete_bulk_roles(self) -> None:
        """Test case for delete_bulk_roles

        Delete Role(s)
        """
        pass

    def test_delete_metadata_from_role_by_key_and_value(self) -> None:
        """Test case for delete_metadata_from_role_by_key_and_value

        Remove a Metadata From Role.
        """
        pass

    def test_delete_role(self) -> None:
        """Test case for delete_role

        Delete a Role
        """
        pass

    def test_get_bulk_update_status(self) -> None:
        """Test case for get_bulk_update_status

        Get Bulk-Update Statuses
        """
        pass

    def test_get_bulk_update_status_by_id(self) -> None:
        """Test case for get_bulk_update_status_by_id

        Get Bulk-Update Status by ID
        """
        pass

    def test_get_role(self) -> None:
        """Test case for get_role

        Get a Role
        """
        pass

    def test_get_role_assigned_identities(self) -> None:
        """Test case for get_role_assigned_identities

        List Identities assigned a Role
        """
        pass

    def test_get_role_entitlements(self) -> None:
        """Test case for get_role_entitlements

        List Role's Entitlements
        """
        pass

    def test_list_roles(self) -> None:
        """Test case for list_roles

        List Roles
        """
        pass

    def test_patch_role(self) -> None:
        """Test case for patch_role

        Patch a specified Role
        """
        pass

    def test_search_roles_by_filter(self) -> None:
        """Test case for search_roles_by_filter

        Filter Roles by Metadata
        """
        pass

    def test_update_attribute_key_and_value_to_role(self) -> None:
        """Test case for update_attribute_key_and_value_to_role

        Add a Metadata to Role.
        """
        pass

    def test_update_roles_metadata_by_filter(self) -> None:
        """Test case for update_roles_metadata_by_filter

        Bulk-Update Roles' Metadata by Filters
        """
        pass

    def test_update_roles_metadata_by_ids(self) -> None:
        """Test case for update_roles_metadata_by_ids

        Bulk-Update Roles' Metadata by ID
        """
        pass

    def test_update_roles_metadata_by_query(self) -> None:
        """Test case for update_roles_metadata_by_query

        Bulk-Update Roles' Metadata by Query
        """
        pass


if __name__ == '__main__':
    unittest.main()
