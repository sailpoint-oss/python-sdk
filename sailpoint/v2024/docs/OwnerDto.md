# OwnerDto

Owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner&#39;s DTO type. | [optional] 
**id** | **str** | Owner&#39;s identity ID. | [optional] 
**name** | **str** | Owner&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.owner_dto import OwnerDto

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerDto from a JSON string
owner_dto_instance = OwnerDto.from_json(json)
# print the JSON string representation of the object
print(OwnerDto.to_json())

# convert the object into a dict
owner_dto_dict = owner_dto_instance.to_dict()
# create an instance of OwnerDto from a dict
owner_dto_from_dict = OwnerDto.from_dict(owner_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


