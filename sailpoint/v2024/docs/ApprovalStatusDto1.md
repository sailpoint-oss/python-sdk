# ApprovalStatusDto1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | True if the request for this item was forwarded from one owner to another. | [optional] [default to False]
**original_owner** | [**ApprovalStatusDtoOriginalOwner**](ApprovalStatusDtoOriginalOwner.md) |  | [optional] 
**current_owner** | [**ApprovalStatusDtoCurrentOwner**](ApprovalStatusDtoCurrentOwner.md) |  | [optional] 
**modified** | **datetime** | Time at which item was modified. | [optional] 
**status** | [**ManualWorkItemState**](ManualWorkItemState.md) |  | [optional] 
**scheme** | [**ApprovalScheme**](ApprovalScheme.md) |  | [optional] 
**error_messages** | [**List[ErrorMessageDto1]**](ErrorMessageDto1.md) | If the request failed, includes any error messages that were generated. | [optional] 
**comment** | **str** | Comment, if any, provided by the approver. | [optional] 
**remove_date** | **datetime** | The date the role or access profile or entitlement is no longer assigned to the specified identity. | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_status_dto1 import ApprovalStatusDto1

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStatusDto1 from a JSON string
approval_status_dto1_instance = ApprovalStatusDto1.from_json(json)
# print the JSON string representation of the object
print(ApprovalStatusDto1.to_json())

# convert the object into a dict
approval_status_dto1_dict = approval_status_dto1_instance.to_dict()
# create an instance of ApprovalStatusDto1 from a dict
approval_status_dto1_from_dict = ApprovalStatusDto1.from_dict(approval_status_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


