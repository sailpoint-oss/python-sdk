# IdentityExceptionReportReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_result_id** | **str** | The id of the task result. | [optional] 
**report_name** | **str** | The name of the report. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_exception_report_reference import IdentityExceptionReportReference

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExceptionReportReference from a JSON string
identity_exception_report_reference_instance = IdentityExceptionReportReference.from_json(json)
# print the JSON string representation of the object
print IdentityExceptionReportReference.to_json()

# convert the object into a dict
identity_exception_report_reference_dict = identity_exception_report_reference_instance.to_dict()
# create an instance of IdentityExceptionReportReference from a dict
identity_exception_report_reference_form_dict = identity_exception_report_reference.from_dict(identity_exception_report_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


