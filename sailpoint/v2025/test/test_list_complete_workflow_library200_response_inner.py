# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.list_complete_workflow_library200_response_inner import ListCompleteWorkflowLibrary200ResponseInner

class TestListCompleteWorkflowLibrary200ResponseInner(unittest.TestCase):
    """ListCompleteWorkflowLibrary200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCompleteWorkflowLibrary200ResponseInner:
        """Test ListCompleteWorkflowLibrary200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCompleteWorkflowLibrary200ResponseInner`
        """
        model = ListCompleteWorkflowLibrary200ResponseInner()
        if include_optional:
            return ListCompleteWorkflowLibrary200ResponseInner(
                id = 'sp:compare-boolean',
                name = 'Compare Boolean Values',
                type = 'OPERATOR',
                description = 'Compare two boolean values and decide what happens based on the result.',
                form_fields = [{description=Enter the JSONPath to a value from the input to compare to Variable B., helpText=, label=Variable A, name=variableA.$, required=true, type=text}, {helpText=Select an operation., label=Operation, name=operator, options=[{label=Equals, value=BooleanEquals}], required=true, type=select}, {description=Enter the JSONPath to a value from the input to compare to Variable A., helpText=, label=Variable B, name=variableB.$, required=false, type=text}, {description=Enter True or False., helpText=, label=Variable B, name=variableB, required=false, type=text}],
                example_output = None,
                deprecated = True,
                deprecated_by = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                version_number = 56,
                is_simulation_enabled = True,
                is_dynamic_schema = False,
                output_schema = sailpoint.v2025.models.output_schema.outputSchema(),
                input_example = {changes=[{attribute=department, newValue=marketing, oldValue=sales}, {attribute=manager, newValue={id=ee769173319b41d19ccec6c235423236c, name=mean.guy, type=IDENTITY}, oldValue={id=ee769173319b41d19ccec6c235423237b, name=nice.guy, type=IDENTITY}}, {attribute=email, newValue=john.doe@gmail.com, oldValue=john.doe@hotmail.com}], identity={id=ee769173319b41d19ccec6cea52f237b, name=john.doe, type=IDENTITY}}
            )
        else:
            return ListCompleteWorkflowLibrary200ResponseInner(
        )
        """

    def testListCompleteWorkflowLibrary200ResponseInner(self):
        """Test ListCompleteWorkflowLibrary200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
