# SimIntegrationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**description** | **str** | The description of the integration | [optional] 
**type** | **str** | The integration type | [optional] 
**attributes** | **object** | The attributes map containing the credentials used to configure the integration. | [optional] 
**sources** | **List[str]** | The list of sources (managed resources) | [optional] 
**cluster** | **str** | The cluster/proxy | [optional] 
**status_map** | **object** | Custom mapping between the integration result and the provisioning result | [optional] 
**request** | **object** | Request data to customize desc and body of the created ticket | [optional] 
**before_provisioning_rule** | [**SimIntegrationDetailsAllOfBeforeProvisioningRule**](SimIntegrationDetailsAllOfBeforeProvisioningRule.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.sim_integration_details import SimIntegrationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SimIntegrationDetails from a JSON string
sim_integration_details_instance = SimIntegrationDetails.from_json(json)
# print the JSON string representation of the object
print SimIntegrationDetails.to_json()

# convert the object into a dict
sim_integration_details_dict = sim_integration_details_instance.to_dict()
# create an instance of SimIntegrationDetails from a dict
sim_integration_details_form_dict = sim_integration_details.from_dict(sim_integration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


