# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.form_definition_input import FormDefinitionInput

class TestFormDefinitionInput(unittest.TestCase):
    """FormDefinitionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormDefinitionInput:
        """Test FormDefinitionInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormDefinitionInput`
        """
        model = FormDefinitionInput()
        if include_optional:
            return FormDefinitionInput(
                id = '00000000-0000-0000-0000-000000000000',
                type = 'STRING',
                label = 'input1',
                description = 'A single dynamic scalar value (i.e. number, string, date, etc.) that can be passed into the form for use in conditional logic'
            )
        else:
            return FormDefinitionInput(
        )
        """

    def testFormDefinitionInput(self):
        """Test FormDefinitionInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
