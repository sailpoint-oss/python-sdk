# ClientLogConfigurationDurationMinutes

Client Runtime Logging Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Log configuration&#39;s client ID | [optional] 
**duration_minutes** | **int** | Duration in minutes for log configuration to remain in effect before resetting to defaults. | [optional] [default to 240]
**root_level** | [**StandardLevel**](StandardLevel.md) |  | 
**log_levels** | [**Dict[str, StandardLevel]**](StandardLevel.md) | Mapping of identifiers to Standard Log Level values | [optional] 

## Example

```python
from sailpoint.v3.models.client_log_configuration_duration_minutes import ClientLogConfigurationDurationMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLogConfigurationDurationMinutes from a JSON string
client_log_configuration_duration_minutes_instance = ClientLogConfigurationDurationMinutes.from_json(json)
# print the JSON string representation of the object
print(ClientLogConfigurationDurationMinutes.to_json())

# convert the object into a dict
client_log_configuration_duration_minutes_dict = client_log_configuration_duration_minutes_instance.to_dict()
# create an instance of ClientLogConfigurationDurationMinutes from a dict
client_log_configuration_duration_minutes_from_dict = ClientLogConfigurationDurationMinutes.from_dict(client_log_configuration_duration_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


