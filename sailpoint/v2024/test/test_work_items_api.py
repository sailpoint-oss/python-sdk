# coding: utf-8

"""
    Identity Security Cloud V2024 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2024
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2024.api.work_items_api import WorkItemsApi


class TestWorkItemsApi(unittest.TestCase):
    """WorkItemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkItemsApi()

    def tearDown(self) -> None:
        pass

    def test_approve_approval_item(self) -> None:
        """Test case for approve_approval_item

        Approve an Approval Item
        """
        pass

    def test_approve_approval_items_in_bulk(self) -> None:
        """Test case for approve_approval_items_in_bulk

        Bulk approve Approval Items
        """
        pass

    def test_complete_work_item(self) -> None:
        """Test case for complete_work_item

        Complete a Work Item
        """
        pass

    def test_get_completed_work_items(self) -> None:
        """Test case for get_completed_work_items

        Completed Work Items
        """
        pass

    def test_get_count_completed_work_items(self) -> None:
        """Test case for get_count_completed_work_items

        Count Completed Work Items
        """
        pass

    def test_get_count_work_items(self) -> None:
        """Test case for get_count_work_items

        Count Work Items
        """
        pass

    def test_get_work_item(self) -> None:
        """Test case for get_work_item

        Get a Work Item
        """
        pass

    def test_get_work_items_summary(self) -> None:
        """Test case for get_work_items_summary

        Work Items Summary
        """
        pass

    def test_list_work_items(self) -> None:
        """Test case for list_work_items

        List Work Items
        """
        pass

    def test_reject_approval_item(self) -> None:
        """Test case for reject_approval_item

        Reject an Approval Item
        """
        pass

    def test_reject_approval_items_in_bulk(self) -> None:
        """Test case for reject_approval_items_in_bulk

        Bulk reject Approval Items
        """
        pass

    def test_send_work_item_forward(self) -> None:
        """Test case for send_work_item_forward

        Forward a Work Item
        """
        pass

    def test_submit_account_selection(self) -> None:
        """Test case for submit_account_selection

        Submit Account Selections
        """
        pass


if __name__ == '__main__':
    unittest.main()