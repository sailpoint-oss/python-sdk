# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.api.access_request_approvals_api import AccessRequestApprovalsApi


class TestAccessRequestApprovalsApi(unittest.TestCase):
    """AccessRequestApprovalsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccessRequestApprovalsApi()

    def tearDown(self) -> None:
        pass

    def test_approve_access_request(self) -> None:
        """Test case for approve_access_request

        Approve access request approval
        """
        pass

    def test_forward_access_request(self) -> None:
        """Test case for forward_access_request

        Forward access request approval
        """
        pass

    def test_get_access_request_approval_summary(self) -> None:
        """Test case for get_access_request_approval_summary

        Get access requests approvals number
        """
        pass

    def test_list_access_request_approvers(self) -> None:
        """Test case for list_access_request_approvers

        Access request approvers
        """
        pass

    def test_list_completed_approvals(self) -> None:
        """Test case for list_completed_approvals

        Completed access request approvals list
        """
        pass

    def test_list_pending_approvals(self) -> None:
        """Test case for list_pending_approvals

        Pending access request approvals list
        """
        pass

    def test_reject_access_request(self) -> None:
        """Test case for reject_access_request

        Reject access request approval
        """
        pass


if __name__ == '__main__':
    unittest.main()
