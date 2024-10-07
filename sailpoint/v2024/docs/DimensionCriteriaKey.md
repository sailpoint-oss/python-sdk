# DimensionCriteriaKey

Refers to a specific Identity attribute used in Dimension membership criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DimensionCriteriaKeyType**](DimensionCriteriaKeyType.md) |  | 
**var_property** | **str** | The name of the identity attribute to which the associated criteria applies. | 

## Example

```python
from sailpoint.v2024.models.dimension_criteria_key import DimensionCriteriaKey

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionCriteriaKey from a JSON string
dimension_criteria_key_instance = DimensionCriteriaKey.from_json(json)
# print the JSON string representation of the object
print(DimensionCriteriaKey.to_json())

# convert the object into a dict
dimension_criteria_key_dict = dimension_criteria_key_instance.to_dict()
# create an instance of DimensionCriteriaKey from a dict
dimension_criteria_key_from_dict = DimensionCriteriaKey.from_dict(dimension_criteria_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


