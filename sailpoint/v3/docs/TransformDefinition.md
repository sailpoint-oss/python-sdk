# TransformDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the transform definition. | [optional] 
**attributes** | [**Dict[str, TransformDefinitionAttributesValue]**](TransformDefinitionAttributesValue.md) | Arbitrary key-value pairs to store any metadata for the object | [optional] 

## Example

```python
from sailpoint.v3.models.transform_definition import TransformDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of TransformDefinition from a JSON string
transform_definition_instance = TransformDefinition.from_json(json)
# print the JSON string representation of the object
print TransformDefinition.to_json()

# convert the object into a dict
transform_definition_dict = transform_definition_instance.to_dict()
# create an instance of TransformDefinition from a dict
transform_definition_form_dict = transform_definition.from_dict(transform_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


