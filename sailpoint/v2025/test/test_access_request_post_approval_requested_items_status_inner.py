# coding: utf-8

"""
    Identity Security Cloud V2025 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: v2025
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v2025.models.access_request_post_approval_requested_items_status_inner import AccessRequestPostApprovalRequestedItemsStatusInner

class TestAccessRequestPostApprovalRequestedItemsStatusInner(unittest.TestCase):
    """AccessRequestPostApprovalRequestedItemsStatusInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestPostApprovalRequestedItemsStatusInner:
        """Test AccessRequestPostApprovalRequestedItemsStatusInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestPostApprovalRequestedItemsStatusInner`
        """
        model = AccessRequestPostApprovalRequestedItemsStatusInner()
        if include_optional:
            return AccessRequestPostApprovalRequestedItemsStatusInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                description = 'Access to engineering database',
                type = ACCESS_PROFILE,
                operation = Add,
                comment = 'William needs this access to do his job.',
                client_metadata = {applicationName=My application},
                approval_info = [
                    sailpoint.v2025.models.access_request_post_approval_requested_items_status_inner_approval_info_inner.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner(
                        approval_comment = 'This access looks good.  Approved.', 
                        approval_decision = APPROVED, 
                        approver_name = 'Stephen.Austin', 
                        approver = sailpoint.v2025.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner_approver(
                            type = IDENTITY, ), )
                    ]
            )
        else:
            return AccessRequestPostApprovalRequestedItemsStatusInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                type = ACCESS_PROFILE,
                operation = Add,
                approval_info = [
                    sailpoint.v2025.models.access_request_post_approval_requested_items_status_inner_approval_info_inner.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner(
                        approval_comment = 'This access looks good.  Approved.', 
                        approval_decision = APPROVED, 
                        approver_name = 'Stephen.Austin', 
                        approver = sailpoint.v2025.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner_approver(
                            type = IDENTITY, ), )
                    ],
        )
        """

    def testAccessRequestPostApprovalRequestedItemsStatusInner(self):
        """Test AccessRequestPostApprovalRequestedItemsStatusInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
