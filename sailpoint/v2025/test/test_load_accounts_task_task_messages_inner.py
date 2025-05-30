# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.load_accounts_task_task_messages_inner import LoadAccountsTaskTaskMessagesInner

class TestLoadAccountsTaskTaskMessagesInner(unittest.TestCase):
    """LoadAccountsTaskTaskMessagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoadAccountsTaskTaskMessagesInner:
        """Test LoadAccountsTaskTaskMessagesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoadAccountsTaskTaskMessagesInner`
        """
        model = LoadAccountsTaskTaskMessagesInner()
        if include_optional:
            return LoadAccountsTaskTaskMessagesInner(
                type = 'WARN',
                error = False,
                warning = True,
                key = 'This aggregation failed because the currently running aggregation must complete before the next one can start.',
                localized_text = 'This aggregation failed because the currently running aggregation must complete before the next one can start.'
            )
        else:
            return LoadAccountsTaskTaskMessagesInner(
        )
        """

    def testLoadAccountsTaskTaskMessagesInner(self):
        """Test LoadAccountsTaskTaskMessagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
