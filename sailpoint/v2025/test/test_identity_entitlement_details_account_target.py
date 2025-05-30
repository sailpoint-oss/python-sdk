# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.identity_entitlement_details_account_target import IdentityEntitlementDetailsAccountTarget

class TestIdentityEntitlementDetailsAccountTarget(unittest.TestCase):
    """IdentityEntitlementDetailsAccountTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityEntitlementDetailsAccountTarget:
        """Test IdentityEntitlementDetailsAccountTarget
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityEntitlementDetailsAccountTarget`
        """
        model = IdentityEntitlementDetailsAccountTarget()
        if include_optional:
            return IdentityEntitlementDetailsAccountTarget(
                account_id = 'c5ef070e-92c6-4276-a006-98490f132dec',
                account_name = 'Adalberto.XYZ',
                account_uuid = '2236c29e-68a6-494d-a469-d072172f46cf',
                source_id = '9269d764-8358-4ab9-9748-d4b7418548ca',
                source_name = 'JDBC XYZ Source',
                remove_date = '2035-01-01T12:00:00.000Z',
                assignment_id = '77a5b7b4-262f-4b6a-a2aa-87f84f45f96f',
                revocable = True
            )
        else:
            return IdentityEntitlementDetailsAccountTarget(
        )
        """

    def testIdentityEntitlementDetailsAccountTarget(self):
        """Test IdentityEntitlementDetailsAccountTarget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
