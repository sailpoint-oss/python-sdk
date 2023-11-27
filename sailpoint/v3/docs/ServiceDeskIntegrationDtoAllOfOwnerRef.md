# ServiceDeskIntegrationDtoAllOfOwnerRef

Source for Service Desk integration template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of source for service desk integration template. | [optional] 
**id** | **str** | ID of source for service desk integration template. | [optional] 
**name** | **str** | Human-readable name of source for service desk integration template. | [optional] 

## Example

```python
from sailpoint.v3.models.service_desk_integration_dto_all_of_owner_ref import ServiceDeskIntegrationDtoAllOfOwnerRef

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskIntegrationDtoAllOfOwnerRef from a JSON string
service_desk_integration_dto_all_of_owner_ref_instance = ServiceDeskIntegrationDtoAllOfOwnerRef.from_json(json)
# print the JSON string representation of the object
print ServiceDeskIntegrationDtoAllOfOwnerRef.to_json()

# convert the object into a dict
service_desk_integration_dto_all_of_owner_ref_dict = service_desk_integration_dto_all_of_owner_ref_instance.to_dict()
# create an instance of ServiceDeskIntegrationDtoAllOfOwnerRef from a dict
service_desk_integration_dto_all_of_owner_ref_form_dict = service_desk_integration_dto_all_of_owner_ref.from_dict(service_desk_integration_dto_all_of_owner_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


