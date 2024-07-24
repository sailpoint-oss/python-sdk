# CompletedApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The approval id. | [optional] 
**name** | **str** | The name of the approval. | [optional] 
**created** | **datetime** | When the approval was created. | [optional] 
**modified** | **datetime** | When the approval was modified last time. | [optional] 
**request_created** | **datetime** | When the access-request was created. | [optional] 
**request_type** | [**AccessRequestType**](AccessRequestType.md) |  | [optional] 
**requester** | [**AccessItemRequesterDto**](AccessItemRequesterDto.md) |  | [optional] 
**requested_for** | [**RequestedItemStatusRequestedFor**](RequestedItemStatusRequestedFor.md) |  | [optional] 
**reviewed_by** | [**CompletedApprovalReviewedBy**](CompletedApprovalReviewedBy.md) |  | [optional] 
**owner** | [**AccessItemOwnerDto**](AccessItemOwnerDto.md) |  | [optional] 
**requested_object** | [**RequestableObjectReference**](RequestableObjectReference.md) |  | [optional] 
**requester_comment** | [**CommentDto1**](CommentDto1.md) |  | [optional] 
**reviewer_comment** | [**CompletedApprovalReviewerComment**](CompletedApprovalReviewerComment.md) |  | [optional] 
**previous_reviewers_comments** | [**List[CommentDto1]**](CommentDto1.md) | The history of the previous reviewers comments. | [optional] 
**forward_history** | [**List[ApprovalForwardHistory]**](ApprovalForwardHistory.md) | The history of approval forward action. | [optional] 
**comment_required_when_rejected** | **bool** | When true the rejector has to provide comments when rejecting | [optional] [default to False]
**state** | [**CompletedApprovalState**](CompletedApprovalState.md) |  | [optional] 
**remove_date** | **datetime** | The date the role or access profile or entitlement is no longer assigned to the specified identity. | [optional] 
**remove_date_update_requested** | **bool** | If true, then the request was to change the remove date or sunset date. | [optional] [default to False]
**current_remove_date** | **datetime** | The remove date or sunset date that was assigned at the time of the request. | [optional] 
**sod_violation_context** | [**SodViolationContextCheckCompleted1**](SodViolationContextCheckCompleted1.md) |  | [optional] 
**pre_approval_trigger_result** | [**CompletedApprovalPreApprovalTriggerResult**](CompletedApprovalPreApprovalTriggerResult.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs provided during the request. | [optional] 
**requested_accounts** | **str** | Information about the requested accounts | [optional] 
**assignment_context** | **object** |  | [optional] 

## Example

```python
from sailpoint.beta.models.completed_approval import CompletedApproval

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedApproval from a JSON string
completed_approval_instance = CompletedApproval.from_json(json)
# print the JSON string representation of the object
print CompletedApproval.to_json()

# convert the object into a dict
completed_approval_dict = completed_approval_instance.to_dict()
# create an instance of CompletedApproval from a dict
completed_approval_form_dict = completed_approval.from_dict(completed_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


