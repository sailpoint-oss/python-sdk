# BaseReferenceDto1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from beta.models.base_reference_dto1 import BaseReferenceDto1

# TODO update the JSON string below
json = "{}"
# create an instance of BaseReferenceDto1 from a JSON string
base_reference_dto1_instance = BaseReferenceDto1.from_json(json)
# print the JSON string representation of the object
print BaseReferenceDto1.to_json()

# convert the object into a dict
base_reference_dto1_dict = base_reference_dto1_instance.to_dict()
# create an instance of BaseReferenceDto1 from a dict
base_reference_dto1_form_dict = base_reference_dto1.from_dict(base_reference_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


