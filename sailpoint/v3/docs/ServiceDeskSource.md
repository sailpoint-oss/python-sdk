# ServiceDeskSource

Source for Service Desk integration template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of source for service desk integration template. | [optional] 
**id** | **str** | ID of source for service desk integration template. | [optional] 
**name** | **str** | Human-readable name of source for service desk integration template. | [optional] 

## Example

```python
from sailpoint.v3.models.service_desk_source import ServiceDeskSource

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceDeskSource from a JSON string
service_desk_source_instance = ServiceDeskSource.from_json(json)
# print the JSON string representation of the object
print(ServiceDeskSource.to_json())

# convert the object into a dict
service_desk_source_dict = service_desk_source_instance.to_dict()
# create an instance of ServiceDeskSource from a dict
service_desk_source_from_dict = ServiceDeskSource.from_dict(service_desk_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


