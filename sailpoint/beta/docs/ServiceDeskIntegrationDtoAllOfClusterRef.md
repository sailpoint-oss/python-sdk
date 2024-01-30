# ServiceDeskIntegrationDtoAllOfClusterRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source cluster DTO type. | [optional] 
**id** | **str** | Source cluster ID. | [optional] 
**name** | **str** | Source cluster display name. | [optional] 

## Example

```python
from sailpoint.beta.models.service_desk_integration_dto_all_of_cluster_ref import ServiceDeskIntegrationDtoAllOfClusterRef

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationDtoAllOfClusterRef from a JSON string
service_desk_integration_dto_all_of_cluster_ref_instance = ServiceDeskIntegrationDtoAllOfClusterRef.from_json(json)
# print the JSON string representation of the object
print ServiceDeskIntegrationDtoAllOfClusterRef.to_json()

# convert the object into a dict
service_desk_integration_dto_all_of_cluster_ref_dict = service_desk_integration_dto_all_of_cluster_ref_instance.to_dict()
# create an instance of ServiceDeskIntegrationDtoAllOfClusterRef from a dict
service_desk_integration_dto_all_of_cluster_ref_form_dict = service_desk_integration_dto_all_of_cluster_ref.from_dict(service_desk_integration_dto_all_of_cluster_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


