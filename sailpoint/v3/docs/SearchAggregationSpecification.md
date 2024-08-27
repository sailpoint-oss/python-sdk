# SearchAggregationSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregation**](NestedAggregation.md) |  | [optional] 
**metric** | [**MetricAggregation**](MetricAggregation.md) |  | [optional] 
**filter** | [**FilterAggregation**](FilterAggregation.md) |  | [optional] 
**bucket** | [**BucketAggregation**](BucketAggregation.md) |  | [optional] 
**sub_aggregation** | [**SubSearchAggregationSpecification**](SubSearchAggregationSpecification.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.search_aggregation_specification import SearchAggregationSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAggregationSpecification from a JSON string
search_aggregation_specification_instance = SearchAggregationSpecification.from_json(json)
# print the JSON string representation of the object
print(SearchAggregationSpecification.to_json())

# convert the object into a dict
search_aggregation_specification_dict = search_aggregation_specification_instance.to_dict()
# create an instance of SearchAggregationSpecification from a dict
search_aggregation_specification_from_dict = SearchAggregationSpecification.from_dict(search_aggregation_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


