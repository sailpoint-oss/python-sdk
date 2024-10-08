# ReportDetailsArguments

The string-object map(dictionary) with the arguments needed for report processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | Source ID. | 
**source_name** | **str** | Source name. | 
**correlated_only** | **bool** | Flag to specify if only correlated identities are included in report. | [default to False]
**authoritative_source** | **str** | Source ID. | 
**selected_formats** | **List[str]** | Output report file formats. These are formats for calling GET endpoint as query parameter &#39;fileFormat&#39;.  In case report won&#39;t have this argument there will be [&#39;CSV&#39;, &#39;PDF&#39;] as default. | [optional] 
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched. | [optional] 
**query** | **str** | The query using the Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL extended by SailPoint to support Nested queries. | 
**columns** | **str** | Comma separated string consisting of technical attribute names of fields to include in report.  Use &#x60;access.spread&#x60;, &#x60;apps.spread&#x60;, &#x60;accounts.spread&#x60; to include respective identity access details.  Use &#x60;accessProfiles.spread&#x60; to unclude access profile details.  Use &#x60;entitlements.spread&#x60; to include entitlement details.  | [optional] 
**sort** | **List[str]** | The fields to be used to sort the search results. Use + or - to specify the sort direction. | [optional] 

## Example

```python
from sailpoint.v3.models.report_details_arguments import ReportDetailsArguments

# TODO update the JSON string below
json = "{}"
# create an instance of ReportDetailsArguments from a JSON string
report_details_arguments_instance = ReportDetailsArguments.from_json(json)
# print the JSON string representation of the object
print(ReportDetailsArguments.to_json())

# convert the object into a dict
report_details_arguments_dict = report_details_arguments_instance.to_dict()
# create an instance of ReportDetailsArguments from a dict
report_details_arguments_from_dict = ReportDetailsArguments.from_dict(report_details_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


