# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.workgroup_bulk_delete_request import WorkgroupBulkDeleteRequest

class TestWorkgroupBulkDeleteRequest(unittest.TestCase):
    """WorkgroupBulkDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkgroupBulkDeleteRequest:
        """Test WorkgroupBulkDeleteRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkgroupBulkDeleteRequest`
        """
        model = WorkgroupBulkDeleteRequest()
        if include_optional:
            return WorkgroupBulkDeleteRequest(
                ids = [567a697e-885b-495a-afc5-d55e1c23a302, c7b0f7b2-1e78-4063-b294-a555333dacd2]
            )
        else:
            return WorkgroupBulkDeleteRequest(
        )
        """

    def testWorkgroupBulkDeleteRequest(self):
        """Test WorkgroupBulkDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
