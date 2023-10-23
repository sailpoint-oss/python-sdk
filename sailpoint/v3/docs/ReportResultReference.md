# ReportResultReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
**status** | **str** | Status of a violation report | [optional] 

## Example

```python
from v3.models.report_result_reference import ReportResultReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResultReference from a JSON string
report_result_reference_instance = ReportResultReference.from_json(json)
# print the JSON string representation of the object
print ReportResultReference.to_json()

# convert the object into a dict
report_result_reference_dict = report_result_reference_instance.to_dict()
# create an instance of ReportResultReference from a dict
report_result_reference_form_dict = report_result_reference.from_dict(report_result_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


