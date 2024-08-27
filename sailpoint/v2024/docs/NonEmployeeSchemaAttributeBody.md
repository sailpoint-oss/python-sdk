# NonEmployeeSchemaAttributeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the attribute. Only type &#39;TEXT&#39; is supported for custom attributes. | 
**label** | **str** | Label displayed on the UI for this schema attribute. | 
**technical_name** | **str** | The technical name of the attribute. Must be unique per source. | 
**help_text** | **str** | help text displayed by UI. | [optional] 
**placeholder** | **str** | Hint text that fills UI box. | [optional] 
**required** | **bool** | If true, the schema attribute is required for all non-employees in the source | [optional] 

## Example

```python
from sailpoint.v2024.models.non_employee_schema_attribute_body import NonEmployeeSchemaAttributeBody

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSchemaAttributeBody from a JSON string
non_employee_schema_attribute_body_instance = NonEmployeeSchemaAttributeBody.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeSchemaAttributeBody.to_json())

# convert the object into a dict
non_employee_schema_attribute_body_dict = non_employee_schema_attribute_body_instance.to_dict()
# create an instance of NonEmployeeSchemaAttributeBody from a dict
non_employee_schema_attribute_body_from_dict = NonEmployeeSchemaAttributeBody.from_dict(non_employee_schema_attribute_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


