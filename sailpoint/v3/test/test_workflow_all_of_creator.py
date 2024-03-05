# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.workflow_all_of_creator import WorkflowAllOfCreator

class TestWorkflowAllOfCreator(unittest.TestCase):
    """WorkflowAllOfCreator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowAllOfCreator:
        """Test WorkflowAllOfCreator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowAllOfCreator`
        """
        model = WorkflowAllOfCreator()
        if include_optional:
            return WorkflowAllOfCreator(
                type = 'IDENTITY',
                id = '2c7180a46faadee4016fb4e018c20642',
                name = 'Michael Michaels'
            )
        else:
            return WorkflowAllOfCreator(
        )
        """

    def testWorkflowAllOfCreator(self):
        """Test WorkflowAllOfCreator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()