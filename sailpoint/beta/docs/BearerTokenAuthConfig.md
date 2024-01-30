# BearerTokenAuthConfig

Config required if BEARER_TOKEN authentication is used. On response, this field is set to null as to not return secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** | Bearer token | [optional] 

## Example

```python
from sailpoint.beta.models.bearer_token_auth_config import BearerTokenAuthConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BearerTokenAuthConfig from a JSON string
bearer_token_auth_config_instance = BearerTokenAuthConfig.from_json(json)
# print the JSON string representation of the object
print BearerTokenAuthConfig.to_json()

# convert the object into a dict
bearer_token_auth_config_dict = bearer_token_auth_config_instance.to_dict()
# create an instance of BearerTokenAuthConfig from a dict
bearer_token_auth_config_form_dict = bearer_token_auth_config.from_dict(bearer_token_auth_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


