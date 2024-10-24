# ContextAttributeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute | [optional] 
**value** | [**ContextAttributeDtoValue**](ContextAttributeDtoValue.md) |  | [optional] 
**derived** | **bool** | True if the attribute was derived. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.context_attribute_dto import ContextAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeDto from a JSON string
context_attribute_dto_instance = ContextAttributeDto.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeDto.to_json())

# convert the object into a dict
context_attribute_dto_dict = context_attribute_dto_instance.to_dict()
# create an instance of ContextAttributeDto from a dict
context_attribute_dto_from_dict = ContextAttributeDto.from_dict(context_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


