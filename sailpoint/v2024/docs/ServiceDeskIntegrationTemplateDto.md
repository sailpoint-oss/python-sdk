# ServiceDeskIntegrationTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**type** | **str** | The &#39;type&#39; property specifies the type of the Service Desk integration template. | [default to 'Web Service SDIM']
**attributes** | **Dict[str, object]** | The &#39;attributes&#39; property value is a map of attributes available for integrations using this Service Desk integration template. | 
**provisioning_config** | [**ProvisioningConfig**](ProvisioningConfig.md) |  | 

## Example

```python
from sailpoint.v2024.models.service_desk_integration_template_dto import ServiceDeskIntegrationTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationTemplateDto from a JSON string
service_desk_integration_template_dto_instance = ServiceDeskIntegrationTemplateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceDeskIntegrationTemplateDto.to_json())

# convert the object into a dict
service_desk_integration_template_dto_dict = service_desk_integration_template_dto_instance.to_dict()
# create an instance of ServiceDeskIntegrationTemplateDto from a dict
service_desk_integration_template_dto_from_dict = ServiceDeskIntegrationTemplateDto.from_dict(service_desk_integration_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


