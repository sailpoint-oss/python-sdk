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

from sailpoint.v2024.models.identity_document import IdentityDocument

class TestIdentityDocument(unittest.TestCase):
    """IdentityDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityDocument:
        """Test IdentityDocument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityDocument`
        """
        model = IdentityDocument()
        if include_optional:
            return IdentityDocument(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'John Doe',
                type = 'identity',
                display_name = 'Carol.Adams',
                first_name = 'Carol',
                last_name = 'Adams',
                email = 'Carol.Adams@sailpointdemo.com',
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                phone = '+1 440-527-3672',
                synced = '',
                inactive = False,
                protected = False,
                status = 'UNREGISTERED',
                employee_number = '1a2a3d4e',
                manager = sailpoint.v2024.models.identity_document_all_of_manager.IdentityDocument_allOf_manager(
                    id = '2c9180867dfe694b017e208e27c05799', 
                    name = 'Amanda.Ross', 
                    display_name = 'Amanda.Ross', ),
                is_manager = False,
                identity_profile = sailpoint.v2024.models.identity_document_all_of_identity_profile.IdentityDocument_allOf_identityProfile(
                    id = '3bc8ad26b8664945866b31339d1ff7d2', 
                    name = 'HR Employees', ),
                source = sailpoint.v2024.models.identity_document_all_of_source.IdentityDocument_allOf_source(
                    id = '2c91808b6e9e6fb8016eec1a2b6f7b5f', 
                    name = 'ODS-HR-Employees', ),
                attributes = {country=US, firstname=Carol, cloudStatus=UNREGISTERED},
                processing_state = '',
                processing_details = sailpoint.v2024.models.processing_details.ProcessingDetails(
                    date = '2018-06-25T20:22:28.104Z', 
                    stage = 'In Process', 
                    retry_count = 0, 
                    stack_trace = '<stack trace>', 
                    message = '<message>', ),
                accounts = [
                    null
                    ],
                account_count = 3,
                apps = [
                    null
                    ],
                app_count = 2,
                access = [
                    null
                    ],
                access_count = 5,
                entitlement_count = 10,
                role_count = 1,
                access_profile_count = 1,
                owns = [
                    sailpoint.v2024.models.owns.Owns(
                        sources = [
                            sailpoint.v2024.models.reference.Reference(
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'John Doe', )
                            ], 
                        entitlements = [
                            sailpoint.v2024.models.reference.Reference(
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'John Doe', )
                            ], 
                        access_profiles = [
                            
                            ], 
                        roles = [
                            
                            ], 
                        apps = [
                            
                            ], 
                        governance_groups = [
                            
                            ], 
                        fallback_approver = False, )
                    ],
                owns_count = 5,
                tags = [TAG_1, TAG_2]
            )
        else:
            return IdentityDocument(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'John Doe',
                type = 'identity',
        )
        """

    def testIdentityDocument(self):
        """Test IdentityDocument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()