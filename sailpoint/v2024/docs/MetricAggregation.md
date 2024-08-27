# MetricAggregation

The calculation done on the results of the query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the metric aggregate to be included in the result. If the metric aggregation is omitted, the resulting aggregation will be a count of the documents in the search results. | 
**type** | [**MetricType**](MetricType.md) |  | [optional] [default to MetricType.UNIQUE_COUNT]
**var_field** | **str** | The field the calculation is performed on.  Prefix the field name with &#39;@&#39; to reference a nested object.  | 

## Example

```python
from sailpoint.v2024.models.metric_aggregation import MetricAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of MetricAggregation from a JSON string
metric_aggregation_instance = MetricAggregation.from_json(json)
# print the JSON string representation of the object
print(MetricAggregation.to_json())

# convert the object into a dict
metric_aggregation_dict = metric_aggregation_instance.to_dict()
# create an instance of MetricAggregation from a dict
metric_aggregation_from_dict = MetricAggregation.from_dict(metric_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


