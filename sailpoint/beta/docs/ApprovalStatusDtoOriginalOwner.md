# ApprovalStatusDtoOriginalOwner

Identity of orginal approval owner.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of original approval owner&#39;s identity. | [optional] 
**id** | **str** | ID of original approval owner&#39;s identity. | [optional] 
**name** | **str** | Display name of original approval owner. | [optional] 

## Example

```python
from beta.models.approval_status_dto_original_owner import ApprovalStatusDtoOriginalOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStatusDtoOriginalOwner from a JSON string
approval_status_dto_original_owner_instance = ApprovalStatusDtoOriginalOwner.from_json(json)
# print the JSON string representation of the object
print ApprovalStatusDtoOriginalOwner.to_json()

# convert the object into a dict
approval_status_dto_original_owner_dict = approval_status_dto_original_owner_instance.to_dict()
# create an instance of ApprovalStatusDtoOriginalOwner from a dict
approval_status_dto_original_owner_form_dict = approval_status_dto_original_owner.from_dict(approval_status_dto_original_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


