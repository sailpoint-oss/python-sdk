# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v2024.models.access_profile_bulk_delete_request import AccessProfileBulkDeleteRequest

class TestAccessProfileBulkDeleteRequest(unittest.TestCase):
    """AccessProfileBulkDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfileBulkDeleteRequest:
        """Test AccessProfileBulkDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfileBulkDeleteRequest`
        """
        model = AccessProfileBulkDeleteRequest()
        if include_optional:
            return AccessProfileBulkDeleteRequest(
                access_profile_ids = [2c9180847812e0b1017817051919ecca, 2c9180887812e0b201781e129f151816],
                best_effort_only = True
            )
        else:
            return AccessProfileBulkDeleteRequest(
        )
        """

    def testAccessProfileBulkDeleteRequest(self):
        """Test AccessProfileBulkDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()