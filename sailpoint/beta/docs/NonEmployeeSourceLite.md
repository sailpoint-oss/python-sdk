# NonEmployeeSourceLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee source id. | [optional] 
**source_id** | **str** | Source Id associated with this non-employee source. | [optional] 
**name** | **str** | Source name associated with this non-employee source. | [optional] 
**description** | **str** | Source description associated with this non-employee source. | [optional] 

## Example

```python
from sailpoint.beta.models.non_employee_source_lite import NonEmployeeSourceLite

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSourceLite from a JSON string
non_employee_source_lite_instance = NonEmployeeSourceLite.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeSourceLite.to_json())

# convert the object into a dict
non_employee_source_lite_dict = non_employee_source_lite_instance.to_dict()
# create an instance of NonEmployeeSourceLite from a dict
non_employee_source_lite_from_dict = NonEmployeeSourceLite.from_dict(non_employee_source_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


