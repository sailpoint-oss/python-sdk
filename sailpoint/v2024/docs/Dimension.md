# Dimension

A Dimension

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Dimension. This field must be left null when creating a dimension, otherwise a 400 Bad Request error will result. | [optional] 
**name** | **str** | The human-readable display name of the Dimension | 
**created** | **datetime** | Date the Dimension was created | [optional] [readonly] 
**modified** | **datetime** | Date the Dimension was last modified. | [optional] [readonly] 
**description** | **str** | A human-readable description of the Dimension | [optional] 
**owner** | [**OwnerReference**](OwnerReference.md) |  | 
**access_profiles** | [**List[AccessProfileRef]**](AccessProfileRef.md) |  | [optional] 
**entitlements** | [**List[EntitlementRef]**](EntitlementRef.md) |  | [optional] 
**membership** | [**DimensionMembershipSelector**](DimensionMembershipSelector.md) |  | [optional] 
**parent_id** | **str** | The ID of the parent role. This field can be left null when creating a dimension, but if provided, it must match the role ID specified in the path variable of the API call. | [optional] 

## Example

```python
from sailpoint.v2024.models.dimension import Dimension

# TODO update the JSON string below
json = "{}"
# create an instance of Dimension from a JSON string
dimension_instance = Dimension.from_json(json)
# print the JSON string representation of the object
print(Dimension.to_json())

# convert the object into a dict
dimension_dict = dimension_instance.to_dict()
# create an instance of Dimension from a dict
dimension_from_dict = Dimension.from_dict(dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


