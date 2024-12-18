# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.models.launcher_request import LauncherRequest

class TestLauncherRequest(unittest.TestCase):
    """LauncherRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LauncherRequest:
        """Test LauncherRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LauncherRequest`
        """
        model = LauncherRequest()
        if include_optional:
            return LauncherRequest(
                name = 'Group Create',
                description = 'Create a new Active Directory Group',
                type = 'INTERACTIVE_PROCESS',
                disabled = False,
                reference = sailpoint.beta.models.launcher_request_reference.LauncherRequest_reference(
                    type = 'WORKFLOW', 
                    id = '2fd6ff94-2081-4d29-acbc-83a0a2f744a5', ),
                config = '{"workflowId" : "6b42d9be-61b6-46af-827e-ea29ba8aa3d9"}'
            )
        else:
            return LauncherRequest(
                name = 'Group Create',
                description = 'Create a new Active Directory Group',
                type = 'INTERACTIVE_PROCESS',
                disabled = False,
                config = '{"workflowId" : "6b42d9be-61b6-46af-827e-ea29ba8aa3d9"}',
        )
        """

    def testLauncherRequest(self):
        """Test LauncherRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
