# MfaOktaConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_method** | **str** | Mfa method name | [optional] 
**enabled** | **bool** | If MFA method is enabled. | [optional] [default to False]
**host** | **str** | The server host name or IP address of the MFA provider. | [optional] 
**access_key** | **str** | The secret key for authenticating requests to the MFA provider. | [optional] 
**identity_attribute** | **str** | Optional. The name of the attribute for mapping IdentityNow identity to the MFA provider. | [optional] 

## Example

```python
from sailpoint.v3.models.mfa_okta_config import MfaOktaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MfaOktaConfig from a JSON string
mfa_okta_config_instance = MfaOktaConfig.from_json(json)
# print the JSON string representation of the object
print MfaOktaConfig.to_json()

# convert the object into a dict
mfa_okta_config_dict = mfa_okta_config_instance.to_dict()
# create an instance of MfaOktaConfig from a dict
mfa_okta_config_form_dict = mfa_okta_config.from_dict(mfa_okta_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


