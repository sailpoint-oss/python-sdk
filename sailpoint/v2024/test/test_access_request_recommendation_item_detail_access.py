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

from sailpoint.v2024.models.access_request_recommendation_item_detail_access import AccessRequestRecommendationItemDetailAccess

class TestAccessRequestRecommendationItemDetailAccess(unittest.TestCase):
    """AccessRequestRecommendationItemDetailAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestRecommendationItemDetailAccess:
        """Test AccessRequestRecommendationItemDetailAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestRecommendationItemDetailAccess`
        """
        model = AccessRequestRecommendationItemDetailAccess()
        if include_optional:
            return AccessRequestRecommendationItemDetailAccess(
                id = '2c9180835d2e5168015d32f890ca1581',
                type = 'ACCESS_PROFILE',
                name = 'Employee-database-read-write',
                description = 'This item grants an employee read and write access to the database'
            )
        else:
            return AccessRequestRecommendationItemDetailAccess(
        )
        """

    def testAccessRequestRecommendationItemDetailAccess(self):
        """Test AccessRequestRecommendationItemDetailAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()