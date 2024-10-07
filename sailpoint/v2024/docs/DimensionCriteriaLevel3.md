# DimensionCriteriaLevel3

Defines STANDARD type Dimension membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**DimensionCriteriaOperation**](DimensionCriteriaOperation.md) |  | [optional] 
**key** | [**DimensionCriteriaKey**](DimensionCriteriaKey.md) |  | [optional] 
**string_value** | **str** | String value to test the Identity attribute specified in the key w/r/t the specified operation. If this criteria is a leaf node, that is, if the operation is one of EQUALS, this field is required. Otherwise, specifying it is an error. | [optional] 

## Example

```python
from sailpoint.v2024.models.dimension_criteria_level3 import DimensionCriteriaLevel3

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionCriteriaLevel3 from a JSON string
dimension_criteria_level3_instance = DimensionCriteriaLevel3.from_json(json)
# print the JSON string representation of the object
print(DimensionCriteriaLevel3.to_json())

# convert the object into a dict
dimension_criteria_level3_dict = dimension_criteria_level3_instance.to_dict()
# create an instance of DimensionCriteriaLevel3 from a dict
dimension_criteria_level3_from_dict = DimensionCriteriaLevel3.from_dict(dimension_criteria_level3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


