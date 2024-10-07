# DimensionMembershipSelector

When present, specifies that the Dimension is to be granted to Identities which either satisfy specific criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DimensionMembershipSelectorType**](DimensionMembershipSelectorType.md) |  | [optional] 
**criteria** | [**DimensionCriteriaLevel1**](DimensionCriteriaLevel1.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.dimension_membership_selector import DimensionMembershipSelector

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionMembershipSelector from a JSON string
dimension_membership_selector_instance = DimensionMembershipSelector.from_json(json)
# print the JSON string representation of the object
print(DimensionMembershipSelector.to_json())

# convert the object into a dict
dimension_membership_selector_dict = dimension_membership_selector_instance.to_dict()
# create an instance of DimensionMembershipSelector from a dict
dimension_membership_selector_from_dict = DimensionMembershipSelector.from_dict(dimension_membership_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


