# Aggregations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nested** | [**NestedAggregation**](NestedAggregation.md) |  | [optional] 
**metric** | [**MetricAggregation**](MetricAggregation.md) |  | [optional] 
**filter** | [**FilterAggregation**](FilterAggregation.md) |  | [optional] 
**bucket** | [**BucketAggregation**](BucketAggregation.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.aggregations import Aggregations

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregations from a JSON string
aggregations_instance = Aggregations.from_json(json)
# print the JSON string representation of the object
print Aggregations.to_json()

# convert the object into a dict
aggregations_dict = aggregations_instance.to_dict()
# create an instance of Aggregations from a dict
aggregations_form_dict = aggregations.from_dict(aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


