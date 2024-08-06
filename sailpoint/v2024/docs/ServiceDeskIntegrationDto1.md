# ServiceDeskIntegrationDto1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Service Desk integration&#39;s name. The name must be unique. | 
**description** | **str** | Service Desk integration&#39;s description. | 
**type** | **str** | Service Desk integration types:  - ServiceNowSDIM - ServiceNow  | [default to 'ServiceNowSDIM']
**owner_ref** | [**ServiceDeskIntegrationDto1AllOfOwnerRef**](ServiceDeskIntegrationDto1AllOfOwnerRef.md) |  | [optional] 
**cluster_ref** | [**ServiceDeskIntegrationDto1AllOfClusterRef**](ServiceDeskIntegrationDto1AllOfClusterRef.md) |  | [optional] 
**cluster** | **str** | Cluster ID for the Service Desk integration (replaced by clusterRef, retained for backward compatibility). | [optional] 
**managed_sources** | **List[str]** | Source IDs for the Service Desk integration (replaced by provisioningConfig.managedSResourceRefs, but retained here for backward compatibility). | [optional] 
**provisioning_config** | [**ProvisioningConfig1**](ProvisioningConfig1.md) |  | [optional] 
**attributes** | **Dict[str, object]** | Service Desk integration&#39;s attributes. Validation constraints enforced by the implementation. | 
**before_provisioning_rule** | [**ServiceDeskIntegrationDto1AllOfBeforeProvisioningRule**](ServiceDeskIntegrationDto1AllOfBeforeProvisioningRule.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.service_desk_integration_dto1 import ServiceDeskIntegrationDto1

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationDto1 from a JSON string
service_desk_integration_dto1_instance = ServiceDeskIntegrationDto1.from_json(json)
# print the JSON string representation of the object
print ServiceDeskIntegrationDto1.to_json()

# convert the object into a dict
service_desk_integration_dto1_dict = service_desk_integration_dto1_instance.to_dict()
# create an instance of ServiceDeskIntegrationDto1 from a dict
service_desk_integration_dto1_form_dict = service_desk_integration_dto1.from_dict(service_desk_integration_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


