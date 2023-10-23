# ServiceDeskIntegrationDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**description** | **str** | Description of the Service Desk integration | 
**type** | **str** | Service Desk integration types  - ServiceNowSDIM - ServiceNow  | [default to 'ServiceNowSDIM']
**owner_ref** | [**ServiceDeskIntegrationDtoAllOfOwnerRef**](ServiceDeskIntegrationDtoAllOfOwnerRef.md) |  | [optional] 
**cluster_ref** | [**ServiceDeskIntegrationDtoAllOfClusterRef**](ServiceDeskIntegrationDtoAllOfClusterRef.md) |  | [optional] 
**cluster** | **str** | ID of the cluster for the Service Desk integration (replaced by clusterRef, retained for backward compatibility) | [optional] 
**managed_sources** | **List[str]** | Source IDs for the Service Desk integration (replaced by provisioningConfig.managedSResourceRefs, but retained here for backward compatibility) | [optional] 
**provisioning_config** | [**ProvisioningConfig**](ProvisioningConfig.md) |  | [optional] 
**attributes** | **Dict[str, object]** | Attributes of the Service Desk integration.  Validation constraints enforced by the implementation. | 
**before_provisioning_rule** | [**ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule**](ServiceDeskIntegrationDtoAllOfBeforeProvisioningRule.md) |  | [optional] 

## Example

```python
from v3.models.service_desk_integration_dto import ServiceDeskIntegrationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationDto from a JSON string
service_desk_integration_dto_instance = ServiceDeskIntegrationDto.from_json(json)
# print the JSON string representation of the object
print ServiceDeskIntegrationDto.to_json()

# convert the object into a dict
service_desk_integration_dto_dict = service_desk_integration_dto_instance.to_dict()
# create an instance of ServiceDeskIntegrationDto from a dict
service_desk_integration_dto_form_dict = service_desk_integration_dto.from_dict(service_desk_integration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


