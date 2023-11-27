# ProvisioningConfigManagedResourceRefsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object being referenced | [optional] 
**id** | **object** | ID of the source | [optional] 
**name** | **object** | Human-readable display name of the source | [optional] 

## Example

```python
from sailpoint.beta.models.provisioning_config_managed_resource_refs_inner import ProvisioningConfigManagedResourceRefsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfigManagedResourceRefsInner from a JSON string
provisioning_config_managed_resource_refs_inner_instance = ProvisioningConfigManagedResourceRefsInner.from_json(json)
# print the JSON string representation of the object
print ProvisioningConfigManagedResourceRefsInner.to_json()

# convert the object into a dict
provisioning_config_managed_resource_refs_inner_dict = provisioning_config_managed_resource_refs_inner_instance.to_dict()
# create an instance of ProvisioningConfigManagedResourceRefsInner from a dict
provisioning_config_managed_resource_refs_inner_form_dict = provisioning_config_managed_resource_refs_inner.from_dict(provisioning_config_managed_resource_refs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


