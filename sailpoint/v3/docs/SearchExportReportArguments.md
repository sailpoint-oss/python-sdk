# SearchExportReportArguments

Arguments for Search Export report (SEARCH_EXPORT)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched. | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) | The filters to be applied for each filtered field name. | [optional] 
**query** | [**Query**](Query.md) |  | 
**include_nested** | **bool** | Indicates whether nested objects from returned search results should be included. | [optional] [default to True]
**sort** | **List[str]** | The fields to be used to sort the search results. Use + or - to specify the sort direction. | [optional] 
**default_s3_bucket** | **bool** | Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and &#39;s3Bucket&#39; argument is null or absent there will be default s3Bucket assigned to the report. | 
**s3_bucket** | **str** | If you want to be specific you could use this argument with defaultS3Bucket &#x3D; false. | [optional] 

## Example

```python
from sailpoint.v3.models.search_export_report_arguments import SearchExportReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExportReportArguments from a JSON string
search_export_report_arguments_instance = SearchExportReportArguments.from_json(json)
# print the JSON string representation of the object
print SearchExportReportArguments.to_json()

# convert the object into a dict
search_export_report_arguments_dict = search_export_report_arguments_instance.to_dict()
# create an instance of SearchExportReportArguments from a dict
search_export_report_arguments_form_dict = search_export_report_arguments.from_dict(search_export_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


