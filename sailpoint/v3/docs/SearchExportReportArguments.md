# SearchExportReportArguments

Arguments for Search Export report (SEARCH_EXPORT)  The report file generated will be a zip file containing csv files of the search results. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched. | [optional] 
**query** | **str** | The query using the Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL extended by SailPoint to support Nested queries. | 
**columns** | **str** | Comma separated string consisting of technical attribute names of fields to include in report.  Use &#x60;access.spread&#x60;, &#x60;apps.spread&#x60;, &#x60;accounts.spread&#x60; to include respective identity access details.  Use &#x60;accessProfiles.spread&#x60; to unclude access profile details.  Use &#x60;entitlements.spread&#x60; to include entitlement details.  | [optional] 
**sort** | **List[str]** | The fields to be used to sort the search results. Use + or - to specify the sort direction. | [optional] 

## Example

```python
from sailpoint.v3.models.search_export_report_arguments import SearchExportReportArguments

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExportReportArguments from a JSON string
search_export_report_arguments_instance = SearchExportReportArguments.from_json(json)
# print the JSON string representation of the object
print(SearchExportReportArguments.to_json())

# convert the object into a dict
search_export_report_arguments_dict = search_export_report_arguments_instance.to_dict()
# create an instance of SearchExportReportArguments from a dict
search_export_report_arguments_from_dict = SearchExportReportArguments.from_dict(search_export_report_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


