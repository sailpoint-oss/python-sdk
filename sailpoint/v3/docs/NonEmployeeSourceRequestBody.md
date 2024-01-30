# NonEmployeeSourceRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of non-employee source. | 
**description** | **str** | Description of non-employee source. | 
**owner** | [**NonEmployeeIdnUserRequest**](NonEmployeeIdnUserRequest.md) |  | 
**management_workgroup** | **str** | The ID for the management workgroup that contains source sub-admins | [optional] 
**approvers** | [**List[NonEmployeeIdnUserRequest]**](NonEmployeeIdnUserRequest.md) | List of approvers. | [optional] 
**account_managers** | [**List[NonEmployeeIdnUserRequest]**](NonEmployeeIdnUserRequest.md) | List of account managers. | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_source_request_body import NonEmployeeSourceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeSourceRequestBody from a JSON string
non_employee_source_request_body_instance = NonEmployeeSourceRequestBody.from_json(json)
# print the JSON string representation of the object
print NonEmployeeSourceRequestBody.to_json()

# convert the object into a dict
non_employee_source_request_body_dict = non_employee_source_request_body_instance.to_dict()
# create an instance of NonEmployeeSourceRequestBody from a dict
non_employee_source_request_body_form_dict = non_employee_source_request_body.from_dict(non_employee_source_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


