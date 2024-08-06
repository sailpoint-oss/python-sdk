# ConfigurationDetailsResponse

The request body of Reassignment Configuration Details for a specific identity and config type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_type** | [**ConfigTypeEnum**](ConfigTypeEnum.md) |  | [optional] 
**target_identity** | [**Identity1**](Identity1.md) |  | [optional] 
**start_date** | **datetime** | The date from which to start reassigning work items | [optional] 
**end_date** | **datetime** | The date from which to stop reassigning work items.  If this is an empty string it indicates a permanent reassignment. | [optional] 
**audit_details** | [**AuditDetails**](AuditDetails.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.configuration_details_response import ConfigurationDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationDetailsResponse from a JSON string
configuration_details_response_instance = ConfigurationDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ConfigurationDetailsResponse.to_json()

# convert the object into a dict
configuration_details_response_dict = configuration_details_response_instance.to_dict()
# create an instance of ConfigurationDetailsResponse from a dict
configuration_details_response_form_dict = configuration_details_response.from_dict(configuration_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


