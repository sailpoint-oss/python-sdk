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

from sailpoint.v2024.models.load_uncorrelated_accounts_task_task_messages_inner import LoadUncorrelatedAccountsTaskTaskMessagesInner

class TestLoadUncorrelatedAccountsTaskTaskMessagesInner(unittest.TestCase):
    """LoadUncorrelatedAccountsTaskTaskMessagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoadUncorrelatedAccountsTaskTaskMessagesInner:
        """Test LoadUncorrelatedAccountsTaskTaskMessagesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoadUncorrelatedAccountsTaskTaskMessagesInner`
        """
        model = LoadUncorrelatedAccountsTaskTaskMessagesInner()
        if include_optional:
            return LoadUncorrelatedAccountsTaskTaskMessagesInner(
                type = 'WARN',
                error = False,
                warning = True,
                key = 'This correlation failed because the currently running correlation must complete before the next one can start.',
                localized_text = 'This correlation failed because the currently running correlation must complete before the next one can start.'
            )
        else:
            return LoadUncorrelatedAccountsTaskTaskMessagesInner(
        )
        """

    def testLoadUncorrelatedAccountsTaskTaskMessagesInner(self):
        """Test LoadUncorrelatedAccountsTaskTaskMessagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()