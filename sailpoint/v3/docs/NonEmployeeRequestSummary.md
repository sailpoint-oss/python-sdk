# NonEmployeeRequestSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **int** | The number of approved non-employee requests on all sources that *requested-for* user manages. | [optional] 
**rejected** | **int** | The number of rejected non-employee requests on all sources that *requested-for* user manages. | [optional] 
**pending** | **int** | The number of pending non-employee requests on all sources that *requested-for* user manages. | [optional] 
**non_employee_count** | **int** | The number of non-employee records on all sources that *requested-for* user manages. | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_request_summary import NonEmployeeRequestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeRequestSummary from a JSON string
non_employee_request_summary_instance = NonEmployeeRequestSummary.from_json(json)
# print the JSON string representation of the object
print NonEmployeeRequestSummary.to_json()

# convert the object into a dict
non_employee_request_summary_dict = non_employee_request_summary_instance.to_dict()
# create an instance of NonEmployeeRequestSummary from a dict
non_employee_request_summary_form_dict = non_employee_request_summary.from_dict(non_employee_request_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


