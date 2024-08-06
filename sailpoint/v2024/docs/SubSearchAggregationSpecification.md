# SubSearchAggregationSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregation**](NestedAggregation.md) |  | [optional] 
**metric** | [**MetricAggregation**](MetricAggregation.md) |  | [optional] 
**filter** | [**FilterAggregation**](FilterAggregation.md) |  | [optional] 
**bucket** | [**BucketAggregation**](BucketAggregation.md) |  | [optional] 
**sub_aggregation** | [**Aggregations**](Aggregations.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.sub_search_aggregation_specification import SubSearchAggregationSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of SubSearchAggregationSpecification from a JSON string
sub_search_aggregation_specification_instance = SubSearchAggregationSpecification.from_json(json)
# print the JSON string representation of the object
print SubSearchAggregationSpecification.to_json()

# convert the object into a dict
sub_search_aggregation_specification_dict = sub_search_aggregation_specification_instance.to_dict()
# create an instance of SubSearchAggregationSpecification from a dict
sub_search_aggregation_specification_form_dict = sub_search_aggregation_specification.from_dict(sub_search_aggregation_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


