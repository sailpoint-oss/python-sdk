# ApprovalStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | True if the request for this item was forwarded from one owner to another. | [optional] [default to False]
**original_owner** | [**ApprovalStatusDtoOriginalOwner**](ApprovalStatusDtoOriginalOwner.md) |  | [optional] 
**current_owner** | [**ApprovalStatusDtoCurrentOwner**](ApprovalStatusDtoCurrentOwner.md) |  | [optional] 
**modified** | **datetime** | Time at which item was modified. | [optional] 
**status** | [**ManualWorkItemState**](ManualWorkItemState.md) |  | [optional] 
**scheme** | [**ApprovalScheme**](ApprovalScheme.md) |  | [optional] 
**error_messages** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) | If the request failed, includes any error messages that were generated. | [optional] 
**comment** | **str** | Comment, if any, provided by the approver. | [optional] 
**remove_date** | **datetime** | The date the role or access profile is no longer assigned to the specified identity. | [optional] 

## Example

```python
from sailpoint.beta.models.approval_status_dto import ApprovalStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStatusDto from a JSON string
approval_status_dto_instance = ApprovalStatusDto.from_json(json)
# print the JSON string representation of the object
print ApprovalStatusDto.to_json()

# convert the object into a dict
approval_status_dto_dict = approval_status_dto_instance.to_dict()
# create an instance of ApprovalStatusDto from a dict
approval_status_dto_form_dict = approval_status_dto.from_dict(approval_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


