# RoleMiningPotentialRoleExportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_entitlement_popularity** | **int** | The minimum popularity among identities in the role which an entitlement must have to be included in the report | [optional] 
**include_common_access** | **bool** | If false, do not include entitlements that are highly popular among the entire orginization | [optional] 
**export_id** | **str** | ID used to reference this export | [optional] 
**status** | [**RoleMiningPotentialRoleExportState**](RoleMiningPotentialRoleExportState.md) |  | [optional] 

## Example

```python
from beta.models.role_mining_potential_role_export_response import RoleMiningPotentialRoleExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleExportResponse from a JSON string
role_mining_potential_role_export_response_instance = RoleMiningPotentialRoleExportResponse.from_json(json)
# print the JSON string representation of the object
print RoleMiningPotentialRoleExportResponse.to_json()

# convert the object into a dict
role_mining_potential_role_export_response_dict = role_mining_potential_role_export_response_instance.to_dict()
# create an instance of RoleMiningPotentialRoleExportResponse from a dict
role_mining_potential_role_export_response_form_dict = role_mining_potential_role_export_response.from_dict(role_mining_potential_role_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


