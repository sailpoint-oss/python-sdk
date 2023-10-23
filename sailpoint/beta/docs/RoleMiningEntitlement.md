# RoleMiningEntitlement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_ref** | [**RoleMiningEntitlementRef**](RoleMiningEntitlementRef.md) |  | [optional] 
**name** | **str** | Name of the entitlement | [optional] 
**application_name** | **str** | Application name of the entitlement | [optional] 
**identity_count** | **int** | The number of identities with this entitlement in a role. | [optional] 
**popularity** | **int** | The % popularity of this entitlement in a role. | [optional] 
**popularity_in_org** | **int** | TThe % popularity of this entitlement in the org. | [optional] 

## Example

```python
from beta.models.role_mining_entitlement import RoleMiningEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningEntitlement from a JSON string
role_mining_entitlement_instance = RoleMiningEntitlement.from_json(json)
# print the JSON string representation of the object
print RoleMiningEntitlement.to_json()

# convert the object into a dict
role_mining_entitlement_dict = role_mining_entitlement_instance.to_dict()
# create an instance of RoleMiningEntitlement from a dict
role_mining_entitlement_form_dict = role_mining_entitlement.from_dict(role_mining_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


