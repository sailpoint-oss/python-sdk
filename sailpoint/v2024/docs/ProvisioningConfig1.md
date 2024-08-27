# ProvisioningConfig1

Specification of a Service Desk integration provisioning configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**universal_manager** | **bool** | Specifies whether this configuration is used to manage provisioning requests for all sources from the org.  If true, no managedResourceRefs are allowed. | [optional] [readonly] [default to False]
**managed_resource_refs** | [**List[ProvisioningConfig1ManagedResourceRefsInner]**](ProvisioningConfig1ManagedResourceRefsInner.md) | References to sources for the Service Desk integration template.  May only be specified if universalManager is false. | [optional] 
**plan_initializer_script** | [**ProvisioningConfig1PlanInitializerScript**](ProvisioningConfig1PlanInitializerScript.md) |  | [optional] 
**no_provisioning_requests** | **bool** | Name of an attribute that when true disables the saving of ProvisioningRequest objects whenever plans are sent through this integration. | [optional] [default to False]
**provisioning_request_expiration** | **int** | When saving pending requests is enabled, this defines the number of hours the request is allowed to live before it is considered expired and no longer affects plan compilation. | [optional] 

## Example

```python
from sailpoint.v2024.models.provisioning_config1 import ProvisioningConfig1

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConfig1 from a JSON string
provisioning_config1_instance = ProvisioningConfig1.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConfig1.to_json())

# convert the object into a dict
provisioning_config1_dict = provisioning_config1_instance.to_dict()
# create an instance of ProvisioningConfig1 from a dict
provisioning_config1_from_dict = ProvisioningConfig1.from_dict(provisioning_config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


