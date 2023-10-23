# BaseReferenceDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the application ID | [optional] 
**name** | **str** | the application name | [optional] 

## Example

```python
from beta.models.base_reference_dto import BaseReferenceDto

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


