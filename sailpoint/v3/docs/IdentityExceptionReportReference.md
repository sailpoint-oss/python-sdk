# IdentityExceptionReportReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_result_id** | **str** | Task result ID. | [optional] 
**report_name** | **str** | Report name. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_exception_report_reference import IdentityExceptionReportReference

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExceptionReportReference from a JSON string
identity_exception_report_reference_instance = IdentityExceptionReportReference.from_json(json)
# print the JSON string representation of the object
print(IdentityExceptionReportReference.to_json())

# convert the object into a dict
identity_exception_report_reference_dict = identity_exception_report_reference_instance.to_dict()
# create an instance of IdentityExceptionReportReference from a dict
identity_exception_report_reference_from_dict = IdentityExceptionReportReference.from_dict(identity_exception_report_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


