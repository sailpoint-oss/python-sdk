# AccessItemRequestedForDto

Identity the access item is requested for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity the access item is requested for. | [optional] 
**id** | **str** | ID of identity the access item is requested for. | [optional] 
**name** | **str** | Human-readable display name of identity the access item is requested for. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_item_requested_for_dto import AccessItemRequestedForDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemRequestedForDto from a JSON string
access_item_requested_for_dto_instance = AccessItemRequestedForDto.from_json(json)
# print the JSON string representation of the object
print AccessItemRequestedForDto.to_json()

# convert the object into a dict
access_item_requested_for_dto_dict = access_item_requested_for_dto_instance.to_dict()
# create an instance of AccessItemRequestedForDto from a dict
access_item_requested_for_dto_form_dict = access_item_requested_for_dto.from_dict(access_item_requested_for_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


