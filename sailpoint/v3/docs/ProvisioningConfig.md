# ProvisioningConfig

Specification of a Service Desk integration provisioning configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**universal_manager** | **bool** | Specifies whether this configuration is used to manage provisioning requests for all sources from the org.  If true, no managedResourceRefs are allowed. | [optional] [readonly] 
**managed_resource_refs** | [**List[ProvisioningConfigManagedResourceRefsInner]**](ProvisioningConfigManagedResourceRefsInner.md) | References to sources for the Service Desk integration template.  May only be specified if universalManager is false. | [optional] 
**plan_initializer_script** | [**ProvisioningConfigPlanInitializerScript**](ProvisioningConfigPlanInitializerScript.md) |  | [optional] 
**no_provisioning_requests** | **bool** | Name of an attribute that when true disables the saving of ProvisioningRequest objects whenever plans are sent through this integration. | [optional] 
**provisioning_request_expiration** | **int** | When saving pending requests is enabled, this defines the number of hours the request is allowed to live before it is considered expired and no longer affects plan compilation. | [optional] 

## Example

```python
from v3.models.provisioning_config import ProvisioningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfig from a JSON string
provisioning_config_instance = ProvisioningConfig.from_json(json)
# print the JSON string representation of the object
print ProvisioningConfig.to_json()

# convert the object into a dict
provisioning_config_dict = provisioning_config_instance.to_dict()
# create an instance of ProvisioningConfig from a dict
provisioning_config_form_dict = provisioning_config.from_dict(provisioning_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


