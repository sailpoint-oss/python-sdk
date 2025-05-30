# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.access_item_removed import AccessItemRemoved

class TestAccessItemRemoved(unittest.TestCase):
    """AccessItemRemoved unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessItemRemoved:
        """Test AccessItemRemoved
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessItemRemoved`
        """
        model = AccessItemRemoved()
        if include_optional:
            return AccessItemRemoved(
                access_item = {id=8c190e6787aa4ed9a90bd9d5344523fb, accessType=account, nativeIdentity=127999, sourceName=JDBC Entitlements Source, entitlementCount=0, displayName=Sample Name},
                identity_id = '8c190e6787aa4ed9a90bd9d5344523fb',
                event_type = 'AccessItemRemoved',
                dt = '2019-03-08T22:37:33.901Z',
                governance_event = sailpoint.v2025.models.correlated_governance_event.CorrelatedGovernanceEvent(
                    name = 'Manager Certification for Jon Snow', 
                    dt = '2019-03-08T22:37:33.901Z', 
                    type = 'certification', 
                    governance_id = '2c91808a77ff216301782327a50f09bf', 
                    owners = [{id=8a80828f643d484f01643e14202e206f, displayName=John Snow}], 
                    reviewers = [{id=8a80828f643d484f01643e14202e206f, displayName=John Snow}], 
                    decision_maker = sailpoint.v2025.models.certifier_response.CertifierResponse(
                        id = '8a80828f643d484f01643e14202e206f', 
                        display_name = 'John Snow', ), )
            )
        else:
            return AccessItemRemoved(
        )
        """

    def testAccessItemRemoved(self):
        """Test AccessItemRemoved"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
