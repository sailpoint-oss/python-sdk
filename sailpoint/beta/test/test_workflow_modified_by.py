# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.workflow_modified_by import WorkflowModifiedBy

class TestWorkflowModifiedBy(unittest.TestCase):
    """WorkflowModifiedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowModifiedBy:
        """Test WorkflowModifiedBy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowModifiedBy`
        """
        model = WorkflowModifiedBy()
        if include_optional:
            return WorkflowModifiedBy(
                type = 'IDENTITY',
                id = '2c9180a46faadee4016fb4e018c20639',
                name = 'Thomas Edison'
            )
        else:
            return WorkflowModifiedBy(
        )
        """

    def testWorkflowModifiedBy(self):
        """Test WorkflowModifiedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()