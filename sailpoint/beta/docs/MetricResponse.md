# MetricResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the name of metric | [optional] 
**value** | **float** | the value associated to the metric | [optional] 

## Example

```python
from sailpoint.beta.models.metric_response import MetricResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetricResponse from a JSON string
metric_response_instance = MetricResponse.from_json(json)
# print the JSON string representation of the object
print(MetricResponse.to_json())

# convert the object into a dict
metric_response_dict = metric_response_instance.to_dict()
# create an instance of MetricResponse from a dict
metric_response_from_dict = MetricResponse.from_dict(metric_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


