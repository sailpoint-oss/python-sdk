# Search


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | [**List[Index]**](Index.md) | The names of the Elasticsearch indices in which to search. If none are provided, then all indices will be searched. | [optional] 
**query_type** | [**QueryType**](QueryType.md) |  | [optional] [default to QueryType.SAILPOINT]
**query_version** | **str** |  | [optional] 
**query** | [**Query**](Query.md) |  | [optional] 
**query_dsl** | **object** | The search query using the Elasticsearch [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/query-dsl.html) syntax. | [optional] 
**text_query** | [**TextQuery**](TextQuery.md) |  | [optional] 
**type_ahead_query** | [**TypeAheadQuery**](TypeAheadQuery.md) |  | [optional] 
**include_nested** | **bool** | Indicates whether nested objects from returned search results should be included. | [optional] [default to True]
**query_result_filter** | [**QueryResultFilter**](QueryResultFilter.md) |  | [optional] 
**aggregation_type** | [**AggregationType**](AggregationType.md) |  | [optional] [default to AggregationType.DSL]
**aggregations_version** | **str** |  | [optional] 
**aggregations_dsl** | **object** | The aggregation search query using Elasticsearch [Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/search-aggregations.html) syntax. | [optional] 
**aggregations** | [**SearchAggregationSpecification**](SearchAggregationSpecification.md) |  | [optional] 
**sort** | **List[str]** | The fields to be used to sort the search results. Use + or - to specify the sort direction. | [optional] 
**search_after** | **List[str]** | Used to begin the search window at the values specified. This parameter consists of the last values of the sorted fields in the current record set. This is used to expand the Elasticsearch limit of 10K records by shifting the 10K window to begin at this value. It is recommended that you always include the ID of the object in addition to any other fields on this parameter in order to ensure you don&#39;t get duplicate results while paging. For example, when searching for identities, if you are sorting by displayName you will also want to include ID, for example [\&quot;displayName\&quot;, \&quot;id\&quot;].  If the last identity ID in the search result is 2c91808375d8e80a0175e1f88a575221 and the last displayName is \&quot;John Doe\&quot;, then using that displayName and ID will start a new search after this identity. The searchAfter value will look like [\&quot;John Doe\&quot;,\&quot;2c91808375d8e80a0175e1f88a575221\&quot;] | [optional] 
**filters** | [**Dict[str, Filter]**](Filter.md) | The filters to be applied for each filtered field name. | [optional] 

## Example

```python
from sailpoint.v3.models.search import Search

# TODO update the JSON string below
json = "{}"
# create an instance of Search from a JSON string
search_instance = Search.from_json(json)
# print the JSON string representation of the object
print(Search.to_json())

# convert the object into a dict
search_dict = search_instance.to_dict()
# create an instance of Search from a dict
search_from_dict = Search.from_dict(search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


