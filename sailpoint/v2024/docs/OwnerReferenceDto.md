# OwnerReferenceDto

Simplified DTO for the owner object of the entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The owner id for the entitlement | [optional] 
**name** | **str** | The owner name for the entitlement | [optional] 
**type** | **str** | The type of the owner. Initially only type IDENTITY is supported | [optional] 

## Example

```python
from sailpoint.v2024.models.owner_reference_dto import OwnerReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerReferenceDto from a JSON string
owner_reference_dto_instance = OwnerReferenceDto.from_json(json)
# print the JSON string representation of the object
print OwnerReferenceDto.to_json()

# convert the object into a dict
owner_reference_dto_dict = owner_reference_dto_instance.to_dict()
# create an instance of OwnerReferenceDto from a dict
owner_reference_dto_form_dict = owner_reference_dto.from_dict(owner_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


