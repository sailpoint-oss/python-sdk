# AccessItemOwnerDto

Access item owner's identity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Access item owner&#39;s DTO type. | [optional] 
**id** | **str** | Access item owner&#39;s identity ID. | [optional] 
**name** | **str** | Access item owner&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.beta.models.access_item_owner_dto import AccessItemOwnerDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessItemOwnerDto from a JSON string
access_item_owner_dto_instance = AccessItemOwnerDto.from_json(json)
# print the JSON string representation of the object
print AccessItemOwnerDto.to_json()

# convert the object into a dict
access_item_owner_dto_dict = access_item_owner_dto_instance.to_dict()
# create an instance of AccessItemOwnerDto from a dict
access_item_owner_dto_form_dict = access_item_owner_dto.from_dict(access_item_owner_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


