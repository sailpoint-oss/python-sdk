# RoleMiningPotentialRoleExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_entitlement_popularity** | **int** | The minimum popularity among identities in the role which an entitlement must have to be included in the report | [optional] 
**include_common_access** | **bool** | If false, do not include entitlements that are highly popular among the entire orginization | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_potential_role_export_request import RoleMiningPotentialRoleExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningPotentialRoleExportRequest from a JSON string
role_mining_potential_role_export_request_instance = RoleMiningPotentialRoleExportRequest.from_json(json)
# print the JSON string representation of the object
print RoleMiningPotentialRoleExportRequest.to_json()

# convert the object into a dict
role_mining_potential_role_export_request_dict = role_mining_potential_role_export_request_instance.to_dict()
# create an instance of RoleMiningPotentialRoleExportRequest from a dict
role_mining_potential_role_export_request_form_dict = role_mining_potential_role_export_request.from_dict(role_mining_potential_role_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


