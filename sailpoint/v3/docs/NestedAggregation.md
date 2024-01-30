# NestedAggregation

The nested aggregation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the nested aggregate to be included in the result. | 
**type** | **str** | The type of the nested object. | 

## Example

```python
from sailpoint.v3.models.nested_aggregation import NestedAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of NestedAggregation from a JSON string
nested_aggregation_instance = NestedAggregation.from_json(json)
# print the JSON string representation of the object
print NestedAggregation.to_json()

# convert the object into a dict
nested_aggregation_dict = nested_aggregation_instance.to_dict()
# create an instance of NestedAggregation from a dict
nested_aggregation_form_dict = nested_aggregation.from_dict(nested_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


