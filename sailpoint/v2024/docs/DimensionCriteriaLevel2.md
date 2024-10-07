# DimensionCriteriaLevel2

Defines STANDARD type Role membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**DimensionCriteriaOperation**](DimensionCriteriaOperation.md) |  | [optional] 
**key** | [**DimensionCriteriaKey**](DimensionCriteriaKey.md) |  | [optional] 
**string_value** | **str** | String value to test the Identity attribute specified in the key w/r/t the specified operation. If this criteria is a leaf node, that is, if the operation is one of EQUALS, this field is required. Otherwise, specifying it is an error. | [optional] 
**children** | [**List[DimensionCriteriaLevel3]**](DimensionCriteriaLevel3.md) | Array of child criteria. Required if the operation is AND or OR, otherwise it must be left null. A maximum of three levels of criteria are supported, including leaf nodes. Additionally, AND nodes can only be children or OR nodes and vice-versa. | [optional] 

## Example

```python
from sailpoint.v2024.models.dimension_criteria_level2 import DimensionCriteriaLevel2

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionCriteriaLevel2 from a JSON string
dimension_criteria_level2_instance = DimensionCriteriaLevel2.from_json(json)
# print the JSON string representation of the object
print(DimensionCriteriaLevel2.to_json())

# convert the object into a dict
dimension_criteria_level2_dict = dimension_criteria_level2_instance.to_dict()
# create an instance of DimensionCriteriaLevel2 from a dict
dimension_criteria_level2_from_dict = DimensionCriteriaLevel2.from_dict(dimension_criteria_level2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


