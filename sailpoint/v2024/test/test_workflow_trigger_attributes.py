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

from sailpoint.v2024.models.workflow_trigger_attributes import WorkflowTriggerAttributes

class TestWorkflowTriggerAttributes(unittest.TestCase):
    """WorkflowTriggerAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowTriggerAttributes:
        """Test WorkflowTriggerAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowTriggerAttributes`
        """
        model = WorkflowTriggerAttributes()
        if include_optional:
            return WorkflowTriggerAttributes(
                id = 'idn:identity-attributes-changed',
                filter_ = '$.changes[?(@.attribute == 'manager')]',
                description = 'Run a search and notify the results',
                name = 'search-and-notify',
                client_id = '87e239b2-b85b-4bde-b9a7-55bf304ddcdc',
                url = 'https://tenant.api.identitynow.com/beta/workflows/execute/external/c79e0079-562c-4df5-aa73-60a9e25c916d',
                cron_string = '0 9 * * 1',
                frequency = 'daily',
                time_zone = 'America/Chicago',
                weekly_days = Monday,
                weekly_times = Monday
            )
        else:
            return WorkflowTriggerAttributes(
                id = 'idn:identity-attributes-changed',
                frequency = 'daily',
        )
        """

    def testWorkflowTriggerAttributes(self):
        """Test WorkflowTriggerAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()