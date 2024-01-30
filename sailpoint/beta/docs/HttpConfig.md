# HttpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the external/custom integration. | 
**http_dispatch_mode** | [**HttpDispatchMode**](HttpDispatchMode.md) |  | 
**http_authentication_type** | [**HttpAuthenticationType**](HttpAuthenticationType.md) |  | [optional] 
**basic_auth_config** | [**BasicAuthConfig**](BasicAuthConfig.md) |  | [optional] 
**bearer_token_auth_config** | [**BearerTokenAuthConfig**](BearerTokenAuthConfig.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.http_config import HttpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConfig from a JSON string
http_config_instance = HttpConfig.from_json(json)
# print the JSON string representation of the object
print HttpConfig.to_json()

# convert the object into a dict
http_config_dict = http_config_instance.to_dict()
# create an instance of HttpConfig from a dict
http_config_form_dict = http_config.from_dict(http_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


