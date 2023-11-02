# PendingApproval


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
**requested_for** | [**AccessItemRequestedForDto**](AccessItemRequestedForDto.md) |  | [optional] 
**owner** | [**AccessItemOwnerDto**](AccessItemOwnerDto.md) |  | [optional] 
**requested_object** | [**RequestableObjectReference**](RequestableObjectReference.md) |  | [optional] 
**requester_comment** | [**CommentDto**](CommentDto.md) |  | [optional] 
**previous_reviewers_comments** | [**List[CommentDto]**](CommentDto.md) | The history of the previous reviewers comments. | [optional] 
**forward_history** | [**List[ApprovalForwardHistory]**](ApprovalForwardHistory.md) | The history of approval forward action. | [optional] 
**comment_required_when_rejected** | **bool** | When true the rejector has to provide comments when rejecting | [optional] 
**action_in_process** | [**PendingApprovalAction**](PendingApprovalAction.md) |  | [optional] 
**remove_date** | **datetime** | The date the role or access profile is no longer assigned to the specified identity. | [optional] 
**remove_date_update_requested** | **bool** | If true, then the request is to change the remove date or sunset date. | [optional] 
**current_remove_date** | **datetime** | The remove date or sunset date that was assigned at the time of the request. | [optional] 
**sod_violation_context** | [**SodViolationContextCheckCompleted1**](SodViolationContextCheckCompleted1.md) |  | [optional] 

## Example

```python
from beta.models.pending_approval import PendingApproval

# TODO update the JSON string below
json = "{}"
# create an instance of PendingApproval from a JSON string
pending_approval_instance = PendingApproval.from_json(json)
# print the JSON string representation of the object
print PendingApproval.to_json()

# convert the object into a dict
pending_approval_dict = pending_approval_instance.to_dict()
# create an instance of PendingApproval from a dict
pending_approval_form_dict = pending_approval.from_dict(pending_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


