# QueryResultFilter

Allows the query results to be filtered by specifying a list of fields to include and/or exclude from the result documents.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includes** | **List[str]** | The list of field names to include in the result documents. | [optional] 
**excludes** | **List[str]** | The list of field names to exclude from the result documents. | [optional] 

## Example

```python
from sailpoint.v3.models.query_result_filter import QueryResultFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryResultFilter from a JSON string
query_result_filter_instance = QueryResultFilter.from_json(json)
# print the JSON string representation of the object
print(QueryResultFilter.to_json())

# convert the object into a dict
query_result_filter_dict = query_result_filter_instance.to_dict()
# create an instance of QueryResultFilter from a dict
query_result_filter_from_dict = QueryResultFilter.from_dict(query_result_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


