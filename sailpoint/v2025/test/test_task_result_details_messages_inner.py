# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.task_result_details_messages_inner import TaskResultDetailsMessagesInner

class TestTaskResultDetailsMessagesInner(unittest.TestCase):
    """TaskResultDetailsMessagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskResultDetailsMessagesInner:
        """Test TaskResultDetailsMessagesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskResultDetailsMessagesInner`
        """
        model = TaskResultDetailsMessagesInner()
        if include_optional:
            return TaskResultDetailsMessagesInner(
                type = 'WARN',
                error = False,
                warning = True,
                key = 'The following account(s) failed to correlate: A,B,C',
                localized_text = 'The following account(s) failed to correlate: A,B,C'
            )
        else:
            return TaskResultDetailsMessagesInner(
        )
        """

    def testTaskResultDetailsMessagesInner(self):
        """Test TaskResultDetailsMessagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
