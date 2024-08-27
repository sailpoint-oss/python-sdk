# AttributeDefinitionSchema

A reference to the schema on the source to the attribute values map to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | The object ID this reference applies to. | [optional] 
**name** | **str** | The human-readable display name of the object. | [optional] 

## Example

```python
from sailpoint.beta.models.attribute_definition_schema import AttributeDefinitionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDefinitionSchema from a JSON string
attribute_definition_schema_instance = AttributeDefinitionSchema.from_json(json)
# print the JSON string representation of the object
print(AttributeDefinitionSchema.to_json())

# convert the object into a dict
attribute_definition_schema_dict = attribute_definition_schema_instance.to_dict()
# create an instance of AttributeDefinitionSchema from a dict
attribute_definition_schema_from_dict = AttributeDefinitionSchema.from_dict(attribute_definition_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


