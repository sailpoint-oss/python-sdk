# NonEmployeeApprovalSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **float** | The number of approved non-employee approval requests. | [optional] 
**pending** | **float** | The number of pending non-employee approval requests. | [optional] 
**rejected** | **float** | The number of rejected non-employee approval requests. | [optional] 

## Example

```python
from sailpoint.beta.models.non_employee_approval_summary import NonEmployeeApprovalSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeApprovalSummary from a JSON string
non_employee_approval_summary_instance = NonEmployeeApprovalSummary.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeApprovalSummary.to_json())

# convert the object into a dict
non_employee_approval_summary_dict = non_employee_approval_summary_instance.to_dict()
# create an instance of NonEmployeeApprovalSummary from a dict
non_employee_approval_summary_from_dict = NonEmployeeApprovalSummary.from_dict(non_employee_approval_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


