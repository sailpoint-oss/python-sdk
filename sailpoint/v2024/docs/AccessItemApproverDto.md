# AccessItemApproverDto

Identity who approved the access item request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who approved the access item request. | [optional] 
**id** | **str** | ID of identity who approved the access item request. | [optional] 
**name** | **str** | Human-readable display name of identity who approved the access item request. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_item_approver_dto import AccessItemApproverDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemApproverDto from a JSON string
access_item_approver_dto_instance = AccessItemApproverDto.from_json(json)
# print the JSON string representation of the object
print(AccessItemApproverDto.to_json())

# convert the object into a dict
access_item_approver_dto_dict = access_item_approver_dto_instance.to_dict()
# create an instance of AccessItemApproverDto from a dict
access_item_approver_dto_from_dict = AccessItemApproverDto.from_dict(access_item_approver_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


