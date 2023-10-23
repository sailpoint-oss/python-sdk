# MfaConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If MFA method is enabled. | [optional] 
**host** | **str** | The server host name or IP address of the MFA provider. | [optional] 
**access_key** | **str** | The secret key for authenticating requests to the MFA provider. | [optional] 
**identity_attribute** | **str** | Optional. The name of the attribute for mapping IdentityNow identity to the MFA provider. | [optional] 

## Example

```python
from beta.models.mfa_config import MfaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MfaConfig from a JSON string
mfa_config_instance = MfaConfig.from_json(json)
# print the JSON string representation of the object
print MfaConfig.to_json()

# convert the object into a dict
mfa_config_dict = mfa_config_instance.to_dict()
# create an instance of MfaConfig from a dict
mfa_config_form_dict = mfa_config.from_dict(mfa_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


