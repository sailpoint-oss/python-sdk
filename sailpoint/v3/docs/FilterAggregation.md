# FilterAggregation

An additional filter to constrain the results of the search query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the filter aggregate to be included in the result. | 
**type** | [**SearchFilterType**](SearchFilterType.md) |  | [optional] 
**field** | **str** | The search field to apply the filter to.  Prefix the field name with &#39;@&#39; to reference a nested object.  | 
**value** | **str** | The value to filter on. | 

## Example

```python
from v3.models.filter_aggregation import FilterAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of FilterAggregation from a JSON string
filter_aggregation_instance = FilterAggregation.from_json(json)
# print the JSON string representation of the object
print FilterAggregation.to_json()

# convert the object into a dict
filter_aggregation_dict = filter_aggregation_instance.to_dict()
# create an instance of FilterAggregation from a dict
filter_aggregation_form_dict = filter_aggregation.from_dict(filter_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


