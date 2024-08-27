# RoleMiningEntitlementRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the entitlement | [optional] 
**name** | **str** | Name of the entitlement | [optional] 
**description** | **str** | Description forthe entitlement | [optional] 
**attribute** | **str** | The entitlement attribute | [optional] 

## Example

```python
from sailpoint.beta.models.role_mining_entitlement_ref import RoleMiningEntitlementRef

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMiningEntitlementRef from a JSON string
role_mining_entitlement_ref_instance = RoleMiningEntitlementRef.from_json(json)
# print the JSON string representation of the object
print(RoleMiningEntitlementRef.to_json())

# convert the object into a dict
role_mining_entitlement_ref_dict = role_mining_entitlement_ref_instance.to_dict()
# create an instance of RoleMiningEntitlementRef from a dict
role_mining_entitlement_ref_from_dict = RoleMiningEntitlementRef.from_dict(role_mining_entitlement_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


