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

from sailpoint.v2024.models.role_mining_potential_role_export_response import RoleMiningPotentialRoleExportResponse

class TestRoleMiningPotentialRoleExportResponse(unittest.TestCase):
    """RoleMiningPotentialRoleExportResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleMiningPotentialRoleExportResponse:
        """Test RoleMiningPotentialRoleExportResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleMiningPotentialRoleExportResponse`
        """
        model = RoleMiningPotentialRoleExportResponse()
        if include_optional:
            return RoleMiningPotentialRoleExportResponse(
                min_entitlement_popularity = 0,
                include_common_access = True,
                export_id = '0c6cdb76-1227-4aaf-af21-192dbdfbfa04',
                status = 'QUEUED'
            )
        else:
            return RoleMiningPotentialRoleExportResponse(
        )
        """

    def testRoleMiningPotentialRoleExportResponse(self):
        """Test RoleMiningPotentialRoleExportResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()