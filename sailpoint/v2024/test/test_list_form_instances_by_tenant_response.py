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

from sailpoint.v2024.models.list_form_instances_by_tenant_response import ListFormInstancesByTenantResponse

class TestListFormInstancesByTenantResponse(unittest.TestCase):
    """ListFormInstancesByTenantResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListFormInstancesByTenantResponse:
        """Test ListFormInstancesByTenantResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFormInstancesByTenantResponse`
        """
        model = ListFormInstancesByTenantResponse()
        if include_optional:
            return ListFormInstancesByTenantResponse(
                count = 1,
                results = [
                    sailpoint.v2024.models.form_instance_response.FormInstanceResponse(
                        created = '2023-07-12T20:14:57.744860Z', 
                        created_by = sailpoint.v2024.models.form_instance_created_by.FormInstanceCreatedBy(
                            id = '00000000-0000-0000-0000-000000000000', 
                            type = 'WORKFLOW_EXECUTION', ), 
                        expire = '2023-08-12T20:14:57.74486Z', 
                        form_conditions = [
                            sailpoint.v2024.models.form_condition.FormCondition(
                                rule_operator = 'AND', 
                                rules = [
                                    sailpoint.v2024.models.condition_rule.ConditionRule(
                                        source_type = 'ELEMENT', 
                                        source = 'department', 
                                        operator = 'EQ', 
                                        value_type = 'STRING', 
                                        value = Engineering, )
                                    ], 
                                effects = [
                                    sailpoint.v2024.models.condition_effect.ConditionEffect(
                                        effect_type = 'HIDE', 
                                        config = sailpoint.v2024.models.condition_effect_config.ConditionEffect_config(
                                            default_value_label = 'Access to Remove', 
                                            element = '8110662963316867', ), )
                                    ], )
                            ], 
                        form_data = {department=Engineering}, 
                        form_definition_id = '49841cb8-00a5-4fbd-9888-8bbb28d48331', 
                        form_elements = [
                            sailpoint.v2024.models.form_element.FormElement(
                                id = '00000000-0000-0000-0000-000000000000', 
                                element_type = 'TEXT', 
                                key = 'department', 
                                validations = [
                                    [{validationType=REQUIRED}]
                                    ], )
                            ], 
                        form_errors = [
                            sailpoint.v2024.models.form_error.FormError(
                                key = 'department', 
                                messages = [
                                    sailpoint.v2024.models.error_message_is_the_standard_api_error_response_message_type/.ErrorMessage is the standard API error response message type.(
                                        locale = 'en-US', 
                                        locale_origin = 'DEFAULT', 
                                        text = 'This is an error', )
                                    ], 
                                value = Engineering, )
                            ], 
                        form_input = {input1=Sales}, 
                        id = '06a2d961-07fa-44d1-8d0a-2f6470e30fd2', 
                        modified = '2023-07-12T20:14:57.744860Z', 
                        recipients = [
                            sailpoint.v2024.models.form_instance_recipient.FormInstanceRecipient(
                                id = '00000000-0000-0000-0000-000000000000', 
                                type = 'IDENTITY', )
                            ], 
                        stand_alone_form = False, 
                        stand_alone_form_url = 'https://my-org.identitynow.com/ui/d/forms/00000000-0000-0000-0000-000000000000', 
                        state = 'ASSIGNED', )
                    ]
            )
        else:
            return ListFormInstancesByTenantResponse(
        )
        """

    def testListFormInstancesByTenantResponse(self):
        """Test ListFormInstancesByTenantResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()