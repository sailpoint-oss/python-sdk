# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.models.sod_violation_context1_conflicting_access_criteria import SodViolationContext1ConflictingAccessCriteria

class TestSodViolationContext1ConflictingAccessCriteria(unittest.TestCase):
    """SodViolationContext1ConflictingAccessCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SodViolationContext1ConflictingAccessCriteria:
        """Test SodViolationContext1ConflictingAccessCriteria
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodViolationContext1ConflictingAccessCriteria`
        """
        model = SodViolationContext1ConflictingAccessCriteria()
        if include_optional:
            return SodViolationContext1ConflictingAccessCriteria(
                left_criteria = sailpoint.v2024.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(
                    criteria_list = [
                        sailpoint.v2024.models.sod_exempt_criteria_1.SodExemptCriteria_1(
                            existing = True, 
                            type = 'IDENTITY', 
                            id = '2c918085771e9d3301773b3cb66f6398', 
                            name = 'My HR Entitlement', )
                        ], ),
                right_criteria = sailpoint.v2024.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(
                    criteria_list = [
                        sailpoint.v2024.models.sod_exempt_criteria_1.SodExemptCriteria_1(
                            existing = True, 
                            type = 'IDENTITY', 
                            id = '2c918085771e9d3301773b3cb66f6398', 
                            name = 'My HR Entitlement', )
                        ], )
            )
        else:
            return SodViolationContext1ConflictingAccessCriteria(
        )
        """

    def testSodViolationContext1ConflictingAccessCriteria(self):
        """Test SodViolationContext1ConflictingAccessCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
