# AttributeDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attribute. | [optional] 
**type** | [**AttributeDefinitionType**](AttributeDefinitionType.md) |  | [optional] 
**var_schema** | [**AttributeDefinitionSchema**](AttributeDefinitionSchema.md) |  | [optional] 
**description** | **str** | A human-readable description of the attribute. | [optional] 
**is_multi** | **bool** | Flag indicating whether or not the attribute is multi-valued. | [optional] [default to False]
**is_entitlement** | **bool** | Flag indicating whether or not the attribute is an entitlement. | [optional] [default to False]
**is_group** | **bool** | Flag indicating whether or not the attribute represents a group. This can only be &#x60;true&#x60; if &#x60;isEntitlement&#x60; is also &#x60;true&#x60; **and** there is a schema defined for the attribute.  | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.attribute_definition import AttributeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDefinition from a JSON string
attribute_definition_instance = AttributeDefinition.from_json(json)
# print the JSON string representation of the object
print AttributeDefinition.to_json()

# convert the object into a dict
attribute_definition_dict = attribute_definition_instance.to_dict()
# create an instance of AttributeDefinition from a dict
attribute_definition_form_dict = attribute_definition.from_dict(attribute_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


