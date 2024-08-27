# ApprovalStatusDtoCurrentOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who reviewed the access item request. | [optional] 
**id** | **str** | ID of identity who reviewed the access item request. | [optional] 
**name** | **str** | Human-readable display name of identity who reviewed the access item request. | [optional] 

## Example

```python
from sailpoint.beta.models.approval_status_dto_current_owner import ApprovalStatusDtoCurrentOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStatusDtoCurrentOwner from a JSON string
approval_status_dto_current_owner_instance = ApprovalStatusDtoCurrentOwner.from_json(json)
# print the JSON string representation of the object
print(ApprovalStatusDtoCurrentOwner.to_json())

# convert the object into a dict
approval_status_dto_current_owner_dict = approval_status_dto_current_owner_instance.to_dict()
# create an instance of ApprovalStatusDtoCurrentOwner from a dict
approval_status_dto_current_owner_from_dict = ApprovalStatusDtoCurrentOwner.from_dict(approval_status_dto_current_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


