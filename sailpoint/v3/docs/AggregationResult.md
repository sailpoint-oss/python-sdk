# AggregationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | **object** | The document containing the results of the aggregation. This document is controlled by Elasticsearch and depends on the type of aggregation query that is run.  See Elasticsearch [Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/search-aggregations.html) documentation for information.  | [optional] 
**hits** | **List[object]** | The results of the aggregation search query.  | [optional] 

## Example

```python
from sailpoint.v3.models.aggregation_result import AggregationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationResult from a JSON string
aggregation_result_instance = AggregationResult.from_json(json)
# print the JSON string representation of the object
print(AggregationResult.to_json())

# convert the object into a dict
aggregation_result_dict = aggregation_result_instance.to_dict()
# create an instance of AggregationResult from a dict
aggregation_result_from_dict = AggregationResult.from_dict(aggregation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


