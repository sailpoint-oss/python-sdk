# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.create_form_instance_request import CreateFormInstanceRequest

class TestCreateFormInstanceRequest(unittest.TestCase):
    """CreateFormInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateFormInstanceRequest:
        """Test CreateFormInstanceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFormInstanceRequest`
        """
        model = CreateFormInstanceRequest()
        if include_optional:
            return CreateFormInstanceRequest(
                created_by = sailpoint.v2025.models.form_instance_created_by.FormInstanceCreatedBy(
                    id = '00000000-0000-0000-0000-000000000000', 
                    type = 'WORKFLOW_EXECUTION', ),
                expire = '2023-08-12T20:14:57.74486Z',
                form_definition_id = '00000000-0000-0000-0000-000000000000',
                form_input = {input1=Sales},
                recipients = [
                    sailpoint.v2025.models.form_instance_recipient.FormInstanceRecipient(
                        id = '00000000-0000-0000-0000-000000000000', 
                        type = 'IDENTITY', )
                    ],
                stand_alone_form = False,
                state = 'ASSIGNED',
                ttl = 1571827560
            )
        else:
            return CreateFormInstanceRequest(
                created_by = sailpoint.v2025.models.form_instance_created_by.FormInstanceCreatedBy(
                    id = '00000000-0000-0000-0000-000000000000', 
                    type = 'WORKFLOW_EXECUTION', ),
                expire = '2023-08-12T20:14:57.74486Z',
                form_definition_id = '00000000-0000-0000-0000-000000000000',
                recipients = [
                    sailpoint.v2025.models.form_instance_recipient.FormInstanceRecipient(
                        id = '00000000-0000-0000-0000-000000000000', 
                        type = 'IDENTITY', )
                    ],
        )
        """

    def testCreateFormInstanceRequest(self):
        """Test CreateFormInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
