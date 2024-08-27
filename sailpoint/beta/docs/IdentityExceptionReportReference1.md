# IdentityExceptionReportReference1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_result_id** | **str** | The id of the task result. | [optional] 
**report_name** | **str** | The name of the report. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_exception_report_reference1 import IdentityExceptionReportReference1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityExceptionReportReference1 from a JSON string
identity_exception_report_reference1_instance = IdentityExceptionReportReference1.from_json(json)
# print the JSON string representation of the object
print(IdentityExceptionReportReference1.to_json())

# convert the object into a dict
identity_exception_report_reference1_dict = identity_exception_report_reference1_instance.to_dict()
# create an instance of IdentityExceptionReportReference1 from a dict
identity_exception_report_reference1_from_dict = IdentityExceptionReportReference1.from_dict(identity_exception_report_reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


