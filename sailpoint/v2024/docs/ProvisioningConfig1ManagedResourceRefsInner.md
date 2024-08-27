# ProvisioningConfig1ManagedResourceRefsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object being referenced | [optional] 
**id** | **object** | ID of the source | [optional] 
**name** | **object** | Human-readable display name of the source | [optional] 

## Example

```python
from sailpoint.v2024.models.provisioning_config1_managed_resource_refs_inner import ProvisioningConfig1ManagedResourceRefsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfig1ManagedResourceRefsInner from a JSON string
provisioning_config1_managed_resource_refs_inner_instance = ProvisioningConfig1ManagedResourceRefsInner.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConfig1ManagedResourceRefsInner.to_json())

# convert the object into a dict
provisioning_config1_managed_resource_refs_inner_dict = provisioning_config1_managed_resource_refs_inner_instance.to_dict()
# create an instance of ProvisioningConfig1ManagedResourceRefsInner from a dict
provisioning_config1_managed_resource_refs_inner_from_dict = ProvisioningConfig1ManagedResourceRefsInner.from_dict(provisioning_config1_managed_resource_refs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


