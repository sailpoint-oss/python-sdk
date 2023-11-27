# ModelSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Schema. | [optional] 
**name** | **str** | The name of the Schema. | [optional] 
**native_object_type** | **str** | The name of the object type on the native system that the schema represents. | [optional] 
**identity_attribute** | **str** | The name of the attribute used to calculate the unique identifier for an object in the schema. | [optional] 
**display_attribute** | **str** | The name of the attribute used to calculate the display value for an object in the schema. | [optional] 
**hierarchy_attribute** | **str** | The name of the attribute whose values represent other objects in a hierarchy. Only relevant to group schemas. | [optional] 
**include_permissions** | **bool** | Flag indicating whether or not the include permissions with the object data when aggregating the schema. | [optional] 
**features** | [**List[SourceFeature]**](SourceFeature.md) | The features that the schema supports. | [optional] 
**configuration** | **object** | Holds any extra configuration data that the schema may require. | [optional] 
**attributes** | [**List[AttributeDefinition]**](AttributeDefinition.md) | The attribute definitions which form the schema. | [optional] 
**created** | **datetime** | The date the Schema was created. | [optional] 
**modified** | **datetime** | The date the Schema was last modified. | [optional] 

## Example

```python
from sailpoint.beta.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print ModelSchema.to_json()

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_form_dict = model_schema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


