# ReportDetails

Details about report to be processed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | Use this property to define what report should be processed in the RDE service. | [optional] 
**arguments** | [**ReportDetailsArguments**](ReportDetailsArguments.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.report_details import ReportDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDetails from a JSON string
report_details_instance = ReportDetails.from_json(json)
# print the JSON string representation of the object
print ReportDetails.to_json()

# convert the object into a dict
report_details_dict = report_details_instance.to_dict()
# create an instance of ReportDetails from a dict
report_details_form_dict = report_details.from_dict(report_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


