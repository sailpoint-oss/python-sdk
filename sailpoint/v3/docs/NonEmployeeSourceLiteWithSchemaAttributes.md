# NonEmployeeSourceLiteWithSchemaAttributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee source id. | [optional] 
**source_id** | **str** | Source Id associated with this non-employee source. | [optional] 
**name** | **str** | Source name associated with this non-employee source. | [optional] 
**description** | **str** | Source description associated with this non-employee source. | [optional] 
**schema_attributes** | [**List[NonEmployeeSchemaAttribute]**](NonEmployeeSchemaAttribute.md) | List of schema attributes associated with this non-employee source. | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_source_lite_with_schema_attributes import NonEmployeeSourceLiteWithSchemaAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSourceLiteWithSchemaAttributes from a JSON string
non_employee_source_lite_with_schema_attributes_instance = NonEmployeeSourceLiteWithSchemaAttributes.from_json(json)
# print the JSON string representation of the object
print NonEmployeeSourceLiteWithSchemaAttributes.to_json()

# convert the object into a dict
non_employee_source_lite_with_schema_attributes_dict = non_employee_source_lite_with_schema_attributes_instance.to_dict()
# create an instance of NonEmployeeSourceLiteWithSchemaAttributes from a dict
non_employee_source_lite_with_schema_attributes_form_dict = non_employee_source_lite_with_schema_attributes.from_dict(non_employee_source_lite_with_schema_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


