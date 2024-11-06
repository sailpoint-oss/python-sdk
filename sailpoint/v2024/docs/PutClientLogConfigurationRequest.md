# PutClientLogConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Log configuration&#39;s client ID | [optional] 
**duration_minutes** | **int** | Duration in minutes for log configuration to remain in effect before resetting to defaults. | [optional] [default to 240]
**root_level** | [**StandardLevel**](StandardLevel.md) |  | 
**log_levels** | [**Dict[str, StandardLevel]**](StandardLevel.md) | Mapping of identifiers to Standard Log Level values | [optional] 
**expiration** | **datetime** | Expiration date-time of the log configuration request.  Can be no greater than 24 hours from current date-time. | [optional] 

## Example

```python
from sailpoint.v2024.models.put_client_log_configuration_request import PutClientLogConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientLogConfigurationRequest from a JSON string
put_client_log_configuration_request_instance = PutClientLogConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(PutClientLogConfigurationRequest.to_json())

# convert the object into a dict
put_client_log_configuration_request_dict = put_client_log_configuration_request_instance.to_dict()
# create an instance of PutClientLogConfigurationRequest from a dict
put_client_log_configuration_request_from_dict = PutClientLogConfigurationRequest.from_dict(put_client_log_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


