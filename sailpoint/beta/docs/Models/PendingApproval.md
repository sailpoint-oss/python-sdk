---
id: beta-pending-approval
title: PendingApproval
pagination_label: PendingApproval
sidebar_label: PendingApproval
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PendingApproval', 'BetaPendingApproval'] 
slug: /tools/sdk/python/beta/models/pending-approval
tags: ['SDK', 'Software Development Kit', 'PendingApproval', 'BetaPendingApproval']
---

# PendingApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The approval id. | [optional] 
**name** | **str** | The name of the approval. | [optional] 
**created** | **datetime** | When the approval was created. | [optional] 
**modified** | **datetime** | When the approval was modified last time. | [optional] 
**request_created** | **datetime** | When the access-request was created. | [optional] 
**request_type** | [**AccessRequestType**](access-request-type) |  | [optional] 
**requester** | [**AccessItemRequesterDto**](access-item-requester-dto) |  | [optional] 
**requested_for** | [**AccessItemRequestedForDto**](access-item-requested-for-dto) |  | [optional] 
**owner** | [**AccessItemOwnerDto**](access-item-owner-dto) |  | [optional] 
**requested_object** | [**RequestableObjectReference**](requestable-object-reference) |  | [optional] 
**requester_comment** | [**CommentDto1**](comment-dto1) |  | [optional] 
**previous_reviewers_comments** | [**[]CommentDto1**](comment-dto1) | The history of the previous reviewers comments. | [optional] 
**forward_history** | [**[]ApprovalForwardHistory**](approval-forward-history) | The history of approval forward action. | [optional] 
**comment_required_when_rejected** | **bool** | When true the rejector has to provide comments when rejecting | [optional] [default to False]
**action_in_process** | [**PendingApprovalAction**](pending-approval-action) |  | [optional] 
**remove_date** | **datetime** | The date the role or access profile or entitlement is no longer assigned to the specified identity. | [optional] 
**remove_date_update_requested** | **bool** | If true, then the request is to change the remove date or sunset date. | [optional] [default to False]
**current_remove_date** | **datetime** | The remove date or sunset date that was assigned at the time of the request. | [optional] 
**sod_violation_context** | [**SodViolationContextCheckCompleted1**](sod-violation-context-check-completed1) |  | [optional] 
**client_metadata** | **map[string]str** | Arbitrary key-value pairs, if any were included in the corresponding access request item | [optional] 
**requested_accounts** | [**[]RequestedAccountRef**](requested-account-ref) | The accounts selected by the user for the access to be provisioned on, in case they have multiple accounts on one or more sources. | [optional] 
**privilege_level** | **str** | The privilege level of the requested access item, if applicable. | [optional] 
}

## Example

```python
from sailpoint.beta.models.pending_approval import PendingApproval

pending_approval = PendingApproval(
id='2c9180835d2e5168015d32f890ca1581',
name='Pending approval name',
created='2017-07-11T18:45:37.098Z',
modified='2018-07-25T20:22:28.104Z',
request_created='2017-07-11T18:45:35.098Z',
request_type='GRANT_ACCESS',
requester=sailpoint.beta.models.access_item_requester_dto.Access Item Requester Dto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
requested_for=sailpoint.beta.models.access_item_requested_for_dto.Access Item Requested For Dto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
owner=sailpoint.beta.models.access_item_owner_dto.Access Item Owner Dto(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
requested_object=sailpoint.beta.models.requestable_object_reference.Requestable Object Reference(
                    id = '2c938083633d259901633d25c68c00fa', 
                    name = 'Object Name', 
                    description = 'Object Description', 
                    type = 'ROLE', ),
requester_comment=sailpoint.beta.models.comment_dto.Comment Dto(
                    comment = 'This is a comment.', 
                    created = '2017-07-11T18:45:37.098Z', 
                    author = sailpoint.beta.models.comment_dto_1_author.CommentDto_1_author(
                        type = 'IDENTITY', 
                        id = '2c9180847e25f377017e2ae8cae4650b', 
                        name = 'john.doe', ), ),
previous_reviewers_comments=[
                    sailpoint.beta.models.comment_dto.Comment Dto(
                        comment = 'This is a comment.', 
                        created = '2017-07-11T18:45:37.098Z', 
                        author = sailpoint.beta.models.comment_dto_1_author.CommentDto_1_author(
                            type = 'IDENTITY', 
                            id = '2c9180847e25f377017e2ae8cae4650b', 
                            name = 'john.doe', ), )
                    ],
forward_history=[
                    sailpoint.beta.models.approval_forward_history.Approval Forward History(
                        old_approver_name = 'Frank Mir', 
                        new_approver_name = 'Al Volta', 
                        comment = 'Forwarding from Frank to Al', 
                        modified = '2019-08-23T18:52:57.398Z', 
                        forwarder_name = 'William Wilson', 
                        reassignment_type = 'AUTOMATIC_REASSIGNMENT', )
                    ],
comment_required_when_rejected=True,
action_in_process='APPROVED',
remove_date='2020-07-11T00:00Z',
remove_date_update_requested=True,
current_remove_date='2020-07-11T00:00Z',
sod_violation_context=sailpoint.beta.models.sod_violation_context_check_completed.Sod Violation Context Check Completed(
                    state = 'SUCCESS', 
                    uuid = 'f73d16e9-a038-46c5-b217-1246e15fdbdd', 
                    violation_check_result = sailpoint.beta.models.sod_violation_check_result.Sod Violation Check Result(
                        message = sailpoint.beta.models.error_message_dto.Error Message Dto(
                            locale = 'en-US', 
                            locale_origin = 'DEFAULT', 
                            text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                        client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                        violation_contexts = [
                            sailpoint.beta.models.sod_violation_context.Sod Violation Context(
                                policy = sailpoint.beta.models.sod_policy_dto.Sod Policy Dto(
                                    type = 'SOD_POLICY', 
                                    id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                    name = 'Business SOD Policy', ), 
                                conflicting_access_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria.SodViolationContext_1_conflictingAccessCriteria(
                                    left_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(
                                        criteria_list = [
                                            sailpoint.beta.models.sod_exempt_criteria.Sod Exempt Criteria(
                                                existing = True, 
                                                type = 'IDENTITY', 
                                                id = '2c918085771e9d3301773b3cb66f6398', 
                                                name = 'My HR Entitlement', )
                                            ], ), 
                                    right_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(), ), )
                            ], 
                        violated_policies = [
                            sailpoint.beta.models.sod_policy_dto.Sod Policy Dto(
                                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                name = 'Business SOD Policy', )
                            ], ), ),
client_metadata={customKey1=custom value 1, customKey2=custom value 2},
requested_accounts=[
                    sailpoint.beta.models.requested_account_ref.Requested Account Ref(
                        name = 'Glen.067da3248e914', 
                        type = 'IDENTITY', 
                        account_uuid = '{fab7119e-004f-4822-9c33-b8d570d6c6a6}', 
                        account_id = 'CN=Glen 067da3248e914,OU=YOUROU,OU=org-data-service,DC=YOURDC,DC=local', 
                        source_name = 'Multi Account AD source name', )
                    ],
privilege_level='High'
)

```
[[Back to top]](#) 

