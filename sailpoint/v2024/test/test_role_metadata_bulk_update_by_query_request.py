# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.role_metadata_bulk_update_by_query_request import RoleMetadataBulkUpdateByQueryRequest

class TestRoleMetadataBulkUpdateByQueryRequest(unittest.TestCase):
    """RoleMetadataBulkUpdateByQueryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleMetadataBulkUpdateByQueryRequest:
        """Test RoleMetadataBulkUpdateByQueryRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleMetadataBulkUpdateByQueryRequest`
        """
        model = RoleMetadataBulkUpdateByQueryRequest()
        if include_optional:
            return RoleMetadataBulkUpdateByQueryRequest(
                query = {query"={indices=[roles], queryType=TEXT, textQuery={terms=[test123], fields=[id], matchAny=false, contains=true}, includeNested=false}},
                operation = 'replace',
                replace_scope = 'ALL',
                values = [
                    sailpoint.v2024.models.role_metadata_bulk_update_by_query_request_values_inner.RoleMetadataBulkUpdateByQueryRequest_values_inner(
                        attribute_key = 'iscFederalClassifications', 
                        attribute_value = [topSecret], )
                    ]
            )
        else:
            return RoleMetadataBulkUpdateByQueryRequest(
                query = {query"={indices=[roles], queryType=TEXT, textQuery={terms=[test123], fields=[id], matchAny=false, contains=true}, includeNested=false}},
                operation = 'replace',
                values = [
                    sailpoint.v2024.models.role_metadata_bulk_update_by_query_request_values_inner.RoleMetadataBulkUpdateByQueryRequest_values_inner(
                        attribute_key = 'iscFederalClassifications', 
                        attribute_value = [topSecret], )
                    ],
        )
        """

    def testRoleMetadataBulkUpdateByQueryRequest(self):
        """Test RoleMetadataBulkUpdateByQueryRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()