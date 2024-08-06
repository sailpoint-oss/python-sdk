# NonEmployeeSourceWithNECount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Non-Employee source id. | [optional] 
**source_id** | **str** | Source Id associated with this non-employee source. | [optional] 
**name** | **str** | Source name associated with this non-employee source. | [optional] 
**description** | **str** | Source description associated with this non-employee source. | [optional] 
**approvers** | [**List[NonEmployeeIdentityReferenceWithId]**](NonEmployeeIdentityReferenceWithId.md) | List of approvers | [optional] 
**account_managers** | [**List[NonEmployeeIdentityReferenceWithId]**](NonEmployeeIdentityReferenceWithId.md) | List of account managers | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 
**non_employee_count** | **int** | Number of non-employee records associated with this source. | [optional] 

## Example

```python
from sailpoint.v2024.models.non_employee_source_with_ne_count import NonEmployeeSourceWithNECount

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSourceWithNECount from a JSON string
non_employee_source_with_ne_count_instance = NonEmployeeSourceWithNECount.from_json(json)
# print the JSON string representation of the object
print NonEmployeeSourceWithNECount.to_json()

# convert the object into a dict
non_employee_source_with_ne_count_dict = non_employee_source_with_ne_count_instance.to_dict()
# create an instance of NonEmployeeSourceWithNECount from a dict
non_employee_source_with_ne_count_form_dict = non_employee_source_with_ne_count.from_dict(non_employee_source_with_ne_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


