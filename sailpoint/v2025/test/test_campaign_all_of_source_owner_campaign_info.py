# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.campaign_all_of_source_owner_campaign_info import CampaignAllOfSourceOwnerCampaignInfo

class TestCampaignAllOfSourceOwnerCampaignInfo(unittest.TestCase):
    """CampaignAllOfSourceOwnerCampaignInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignAllOfSourceOwnerCampaignInfo:
        """Test CampaignAllOfSourceOwnerCampaignInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignAllOfSourceOwnerCampaignInfo`
        """
        model = CampaignAllOfSourceOwnerCampaignInfo()
        if include_optional:
            return CampaignAllOfSourceOwnerCampaignInfo(
                source_ids = [0fbe863c063c4c88a35fd7f17e8a3df5]
            )
        else:
            return CampaignAllOfSourceOwnerCampaignInfo(
        )
        """

    def testCampaignAllOfSourceOwnerCampaignInfo(self):
        """Test CampaignAllOfSourceOwnerCampaignInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
