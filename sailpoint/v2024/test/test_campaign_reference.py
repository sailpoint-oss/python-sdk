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

from sailpoint.v2024.models.campaign_reference import CampaignReference

class TestCampaignReference(unittest.TestCase):
    """CampaignReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignReference:
        """Test CampaignReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignReference`
        """
        model = CampaignReference()
        if include_optional:
            return CampaignReference(
                id = 'ef38f94347e94562b5bb8424a56397d8',
                name = 'Campaign Name',
                type = 'CAMPAIGN',
                campaign_type = 'MANAGER',
                description = 'A description of the campaign',
                correlated_status = CORRELATED,
                mandatory_comment_requirement = 'NO_DECISIONS'
            )
        else:
            return CampaignReference(
                id = 'ef38f94347e94562b5bb8424a56397d8',
                name = 'Campaign Name',
                type = 'CAMPAIGN',
                campaign_type = 'MANAGER',
                description = 'A description of the campaign',
                correlated_status = CORRELATED,
                mandatory_comment_requirement = 'NO_DECISIONS',
        )
        """

    def testCampaignReference(self):
        """Test CampaignReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()