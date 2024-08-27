# Range

The range of values to be filtered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower** | [**Bound**](Bound.md) |  | [optional] 
**upper** | [**Bound**](Bound.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print(Range.to_json())

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


