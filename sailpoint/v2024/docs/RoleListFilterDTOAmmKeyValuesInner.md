# RoleListFilterDTOAmmKeyValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | attribute key of a metadata. | [optional] 
**values** | **List[str]** | A list of attribute key names to filter roles. If the values is empty, will only filter by attribute key. | [optional] 

## Example

```python
from sailpoint.v2024.models.role_list_filter_dto_amm_key_values_inner import RoleListFilterDTOAmmKeyValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoleListFilterDTOAmmKeyValuesInner from a JSON string
role_list_filter_dto_amm_key_values_inner_instance = RoleListFilterDTOAmmKeyValuesInner.from_json(json)
# print the JSON string representation of the object
print(RoleListFilterDTOAmmKeyValuesInner.to_json())

# convert the object into a dict
role_list_filter_dto_amm_key_values_inner_dict = role_list_filter_dto_amm_key_values_inner_instance.to_dict()
# create an instance of RoleListFilterDTOAmmKeyValuesInner from a dict
role_list_filter_dto_amm_key_values_inner_from_dict = RoleListFilterDTOAmmKeyValuesInner.from_dict(role_list_filter_dto_amm_key_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


