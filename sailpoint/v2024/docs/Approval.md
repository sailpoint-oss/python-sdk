# Approval

Approval Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_id** | **str** | The Approval ID | [optional] 
**approvers** | [**List[ApprovalIdentity]**](ApprovalIdentity.md) | Object representation of an approver of an approval | [optional] 
**created_date** | **str** | Date the approval was created | [optional] 
**type** | **str** | Type of approval | [optional] 
**name** | [**List[ApprovalName]**](ApprovalName.md) | The name of the approval for a given locale | [optional] 
**batch_request** | [**ApprovalBatch**](.md) | The name of the approval for a given locale | [optional] 
**description** | [**List[ApprovalDescription]**](ApprovalDescription.md) | The description of the approval for a given locale | [optional] 
**priority** | **str** | The priority of the approval | [optional] 
**requester** | [**ApprovalIdentity**](.md) | Object representation of the requester of the approval | [optional] 
**comments** | [**List[ApprovalComment1]**](ApprovalComment1.md) | Object representation of a comment on the approval | [optional] 
**approved_by** | [**List[ApprovalIdentity]**](ApprovalIdentity.md) | Array of approvers who have approved the approval | [optional] 
**rejected_by** | [**List[ApprovalIdentity]**](ApprovalIdentity.md) | Array of approvers who have rejected the approval | [optional] 
**completed_date** | **str** | Date the approval was completed | [optional] 
**approval_criteria** | **str** | Criteria that needs to be met for an approval to be marked as approved | [optional] 
**status** | **str** | The current status of the approval | [optional] 
**additional_attributes** | **str** | Json string representing additional attributes known about the object to be approved. | [optional] 
**reference_data** | [**List[ApprovalReference]**](ApprovalReference.md) | Reference data related to the approval | [optional] 

## Example

```python
from sailpoint.v2024.models.approval import Approval

# TODO update the JSON string below
json = "{}"
# create an instance of Approval from a JSON string
approval_instance = Approval.from_json(json)
# print the JSON string representation of the object
print(Approval.to_json())

# convert the object into a dict
approval_dict = approval_instance.to_dict()
# create an instance of Approval from a dict
approval_from_dict = Approval.from_dict(approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


