# ClientLogConfigurationExpiration

Client Runtime Logging Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Log configuration&#39;s client ID | [optional] 
**expiration** | **datetime** | Expiration date-time of the log configuration request.  Can be no greater than 24 hours from current date-time. | [optional] 
**root_level** | [**StandardLevel**](StandardLevel.md) |  | 
**log_levels** | [**Dict[str, StandardLevel]**](StandardLevel.md) | Mapping of identifiers to Standard Log Level values | [optional] 

## Example

```python
from sailpoint.v2024.models.client_log_configuration_expiration import ClientLogConfigurationExpiration

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLogConfigurationExpiration from a JSON string
client_log_configuration_expiration_instance = ClientLogConfigurationExpiration.from_json(json)
# print the JSON string representation of the object
print(ClientLogConfigurationExpiration.to_json())

# convert the object into a dict
client_log_configuration_expiration_dict = client_log_configuration_expiration_instance.to_dict()
# create an instance of ClientLogConfigurationExpiration from a dict
client_log_configuration_expiration_from_dict = ClientLogConfigurationExpiration.from_dict(client_log_configuration_expiration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


