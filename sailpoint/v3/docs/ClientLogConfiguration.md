# ClientLogConfiguration

Client Runtime Logging Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Log configuration&#39;s client ID | [optional] 
**duration_minutes** | **int** | Duration in minutes for log configuration to remain in effect before resetting to defaults | 
**expiration** | **datetime** | Expiration date-time of the log configuration request | [optional] 
**root_level** | [**StandardLevel**](StandardLevel.md) |  | 
**log_levels** | [**Dict[str, StandardLevel]**](StandardLevel.md) | Mapping of identifiers to Standard Log Level values | [optional] 

## Example

```python
from sailpoint.v3.models.client_log_configuration import ClientLogConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLogConfiguration from a JSON string
client_log_configuration_instance = ClientLogConfiguration.from_json(json)
# print the JSON string representation of the object
print(ClientLogConfiguration.to_json())

# convert the object into a dict
client_log_configuration_dict = client_log_configuration_instance.to_dict()
# create an instance of ClientLogConfiguration from a dict
client_log_configuration_from_dict = ClientLogConfiguration.from_dict(client_log_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


