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

from sailpoint.v2024.models.identity_entities import IdentityEntities

class TestIdentityEntities(unittest.TestCase):
    """IdentityEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityEntities:
        """Test IdentityEntities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityEntities`
        """
        model = IdentityEntities()
        if include_optional:
            return IdentityEntities(
                identity_entity = sailpoint.v2024.models.identity_entities_identity_entity.IdentityEntities_identityEntity(
                    id = '031034e97f094a4096c1be53f75f6b91', 
                    name = 'Gaston.800ddf9640a', 
                    type = 'CAMPAIGN_CAMPAIGNER', )
            )
        else:
            return IdentityEntities(
        )
        """

    def testIdentityEntities(self):
        """Test IdentityEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()