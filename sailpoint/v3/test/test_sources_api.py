# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.api.sources_api import SourcesApi


class TestSourcesApi(unittest.TestCase):
    """SourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SourcesApi()

    def tearDown(self) -> None:
        pass

    def test_create_provisioning_policy(self) -> None:
        """Test case for create_provisioning_policy

        Create provisioning policy
        """
        pass

    def test_create_source(self) -> None:
        """Test case for create_source

        Creates a source in identitynow.
        """
        pass

    def test_create_source_schema(self) -> None:
        """Test case for create_source_schema

        Create schema on source
        """
        pass

    def test_delete_provisioning_policy(self) -> None:
        """Test case for delete_provisioning_policy

        Delete provisioning policy by usagetype
        """
        pass

    def test_delete_source(self) -> None:
        """Test case for delete_source

        Delete source by id
        """
        pass

    def test_delete_source_schema(self) -> None:
        """Test case for delete_source_schema

        Delete source schema by id
        """
        pass

    def test_get_accounts_schema(self) -> None:
        """Test case for get_accounts_schema

        Downloads source accounts schema template
        """
        pass

    def test_get_entitlements_schema(self) -> None:
        """Test case for get_entitlements_schema

        Downloads source entitlements schema template
        """
        pass

    def test_get_provisioning_policy(self) -> None:
        """Test case for get_provisioning_policy

        Get provisioning policy by usagetype
        """
        pass

    def test_get_source(self) -> None:
        """Test case for get_source

        Get source by id
        """
        pass

    def test_get_source_connections(self) -> None:
        """Test case for get_source_connections

        Get source connections by id
        """
        pass

    def test_get_source_health(self) -> None:
        """Test case for get_source_health

        Fetches source health by id
        """
        pass

    def test_get_source_schema(self) -> None:
        """Test case for get_source_schema

        Get source schema by id
        """
        pass

    def test_get_source_schemas(self) -> None:
        """Test case for get_source_schemas

        List schemas on source
        """
        pass

    def test_import_accounts_schema(self) -> None:
        """Test case for import_accounts_schema

        Uploads source accounts schema template
        """
        pass

    def test_import_connector_file(self) -> None:
        """Test case for import_connector_file

        Upload connector file to source
        """
        pass

    def test_import_entitlements_schema(self) -> None:
        """Test case for import_entitlements_schema

        Uploads source entitlements schema template
        """
        pass

    def test_list_provisioning_policies(self) -> None:
        """Test case for list_provisioning_policies

        Lists provisioningpolicies
        """
        pass

    def test_list_sources(self) -> None:
        """Test case for list_sources

        Lists all sources in identitynow.
        """
        pass

    def test_put_provisioning_policy(self) -> None:
        """Test case for put_provisioning_policy

        Update provisioning policy by usagetype
        """
        pass

    def test_put_source(self) -> None:
        """Test case for put_source

        Update source (full)
        """
        pass

    def test_put_source_schema(self) -> None:
        """Test case for put_source_schema

        Update source schema (full)
        """
        pass

    def test_update_provisioning_policies_in_bulk(self) -> None:
        """Test case for update_provisioning_policies_in_bulk

        Bulk update provisioning policies
        """
        pass

    def test_update_provisioning_policy(self) -> None:
        """Test case for update_provisioning_policy

        Partial update of provisioning policy
        """
        pass

    def test_update_source(self) -> None:
        """Test case for update_source

        Update source (partial)
        """
        pass

    def test_update_source_schema(self) -> None:
        """Test case for update_source_schema

        Update source schema (partial)
        """
        pass


if __name__ == '__main__':
    unittest.main()
