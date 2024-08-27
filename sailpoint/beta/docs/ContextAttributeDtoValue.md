# ContextAttributeDtoValue

The value of the attribute.  This can be either a string or a multi-valued string

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.beta.models.context_attribute_dto_value import ContextAttributeDtoValue

# TODO update the JSON string below
json = "{}"
# create an instance of ContextAttributeDtoValue from a JSON string
context_attribute_dto_value_instance = ContextAttributeDtoValue.from_json(json)
# print the JSON string representation of the object
print(ContextAttributeDtoValue.to_json())

# convert the object into a dict
context_attribute_dto_value_dict = context_attribute_dto_value_instance.to_dict()
# create an instance of ContextAttributeDtoValue from a dict
context_attribute_dto_value_from_dict = ContextAttributeDtoValue.from_dict(context_attribute_dto_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


