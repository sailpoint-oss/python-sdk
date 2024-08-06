# BaseReferenceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v2024.models.base_reference_dto import BaseReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseReferenceDto from a JSON string
base_reference_dto_instance = BaseReferenceDto.from_json(json)
# print the JSON string representation of the object
print BaseReferenceDto.to_json()

# convert the object into a dict
base_reference_dto_dict = base_reference_dto_instance.to_dict()
# create an instance of BaseReferenceDto from a dict
base_reference_dto_form_dict = base_reference_dto.from_dict(base_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


