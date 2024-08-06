# ReportResults

Details about report result or current state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | Use this property to define what report should be processed in the RDE service. | [optional] 
**task_def_name** | **str** | Name of the task definition which is started to process requesting report. Usually the same as report name | [optional] 
**id** | **str** | Unique task definition identifier. | [optional] 
**created** | **datetime** | Report processing start date | [optional] 
**status** | **str** | Report current state or result status. | [optional] 
**duration** | **int** | Report processing time in ms. | [optional] 
**rows** | **int** | Report size in rows. | [optional] 
**available_formats** | **List[str]** | Output report file formats. This are formats for calling get endpoint as a query parameter &#39;fileFormat&#39;.  In case report won&#39;t have this argument there will be [&#39;CSV&#39;, &#39;PDF&#39;] as default. | [optional] 

## Example

```python
from sailpoint.v2024.models.report_results import ReportResults

# TODO update the JSON string below
json = "{}"
# create an instance of ReportResults from a JSON string
report_results_instance = ReportResults.from_json(json)
# print the JSON string representation of the object
print ReportResults.to_json()

# convert the object into a dict
report_results_dict = report_results_instance.to_dict()
# create an instance of ReportResults from a dict
report_results_form_dict = report_results.from_dict(report_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


