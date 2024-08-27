# ServiceDeskIntegrationTemplateType

This represents a Service Desk Integration template type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the type. | [optional] 
**type** | **str** | This is the type value for the type. | 
**script_name** | **str** | This is the scriptName attribute value for the type. | 

## Example

```python
from sailpoint.beta.models.service_desk_integration_template_type import ServiceDeskIntegrationTemplateType

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationTemplateType from a JSON string
service_desk_integration_template_type_instance = ServiceDeskIntegrationTemplateType.from_json(json)
# print the JSON string representation of the object
print(ServiceDeskIntegrationTemplateType.to_json())

# convert the object into a dict
service_desk_integration_template_type_dict = service_desk_integration_template_type_instance.to_dict()
# create an instance of ServiceDeskIntegrationTemplateType from a dict
service_desk_integration_template_type_from_dict = ServiceDeskIntegrationTemplateType.from_dict(service_desk_integration_template_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


