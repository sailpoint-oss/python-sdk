# ContextAttributeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute | [optional] 
**value** | [**ContextAttributeDtoValue**](ContextAttributeDtoValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.context_attribute_dto import ContextAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeDto from a JSON string
context_attribute_dto_instance = ContextAttributeDto.from_json(json)
# print the JSON string representation of the object
print ContextAttributeDto.to_json()

# convert the object into a dict
context_attribute_dto_dict = context_attribute_dto_instance.to_dict()
# create an instance of ContextAttributeDto from a dict
context_attribute_dto_form_dict = context_attribute_dto.from_dict(context_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


