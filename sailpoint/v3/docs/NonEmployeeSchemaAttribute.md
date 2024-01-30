# NonEmployeeSchemaAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Schema Attribute Id | [optional] 
**system** | **bool** | True if this schema attribute is mandatory on all non-employees sources. | [optional] 
**modified** | **datetime** | When the schema attribute was last modified. | [optional] 
**created** | **datetime** | When the schema attribute was created. | [optional] 
**type** | [**NonEmployeeSchemaAttributeType**](NonEmployeeSchemaAttributeType.md) |  | 
**label** | **str** | Label displayed on the UI for this schema attribute. | 
**technical_name** | **str** | The technical name of the attribute. Must be unique per source. | 
**help_text** | **str** | help text displayed by UI. | [optional] 
**placeholder** | **str** | Hint text that fills UI box. | [optional] 
**required** | **bool** | If true, the schema attribute is required for all non-employees in the source | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSchemaAttribute from a JSON string
non_employee_schema_attribute_instance = NonEmployeeSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print NonEmployeeSchemaAttribute.to_json()

# convert the object into a dict
non_employee_schema_attribute_dict = non_employee_schema_attribute_instance.to_dict()
# create an instance of NonEmployeeSchemaAttribute from a dict
non_employee_schema_attribute_form_dict = non_employee_schema_attribute.from_dict(non_employee_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


