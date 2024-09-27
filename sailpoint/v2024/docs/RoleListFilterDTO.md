# RoleListFilterDTO

AMMFilterValues

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **str** | Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results) Filtering is supported for the following fields and operators:  **id**: *eq, in*  **name**: *eq, sw*  **created**: *gt, lt, ge, le*  **modified**: *gt, lt, ge, le*  **owner.id**: *eq, in*  **requestable**: *eq* | [optional] 
**amm_key_values** | [**List[RoleListFilterDTOAmmKeyValuesInner]**](RoleListFilterDTOAmmKeyValuesInner.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.role_list_filter_dto import RoleListFilterDTO

# TODO update the JSON string below
json = "{}"
# create an instance of RoleListFilterDTO from a JSON string
role_list_filter_dto_instance = RoleListFilterDTO.from_json(json)
# print the JSON string representation of the object
print(RoleListFilterDTO.to_json())

# convert the object into a dict
role_list_filter_dto_dict = role_list_filter_dto_instance.to_dict()
# create an instance of RoleListFilterDTO from a dict
role_list_filter_dto_from_dict = RoleListFilterDTO.from_dict(role_list_filter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


