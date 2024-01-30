# ReportDetailsArguments

The string-object map(dictionary) with the arguments needed for report processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Id of the authoritative source to export related accounts e.g. identities | 
**source_name** | **str** | Name of the authoritative source for accounts export | 
**default_s3_bucket** | **bool** | Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and &#39;s3Bucket&#39; argument is null or absent there will be default s3Bucket assigned to the report. | 
**s3_bucket** | **str** | If you want to be specific you could use this argument with defaultS3Bucket &#x3D; false. | [optional] 
**correlated_only** | **bool** | Boolean FLAG to specify if only correlated identities should be used in report processing | [default to False]
**authoritative_source** | **str** | Source Id to be checked on errors of identity profiles aggregation | 
**selected_formats** | **List[str]** | Output report file formats. This are formats for calling get endpoint as a query parameter &#39;fileFormat&#39;.  In case report won&#39;t have this argument there will be [&#39;CSV&#39;, &#39;PDF&#39;] as default. | [optional] 
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched. | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) | The filters to be applied for each filtered field name. | [optional] 
**query** | [**Query**](Query.md) |  | 
**include_nested** | **bool** | Indicates whether nested objects from returned search results should be included. | [optional] [default to True]
**sort** | **List[str]** | The fields to be used to sort the search results. Use + or - to specify the sort direction. | [optional] 

## Example

```python
from sailpoint.v3.models.report_details_arguments import ReportDetailsArguments

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDetailsArguments from a JSON string
report_details_arguments_instance = ReportDetailsArguments.from_json(json)
# print the JSON string representation of the object
print ReportDetailsArguments.to_json()

# convert the object into a dict
report_details_arguments_dict = report_details_arguments_instance.to_dict()
# create an instance of ReportDetailsArguments from a dict
report_details_arguments_form_dict = report_details_arguments.from_dict(report_details_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


