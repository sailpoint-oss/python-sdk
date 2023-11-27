# MfaDuoConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_method** | **str** | Mfa method name | [optional] 
**enabled** | **bool** | If MFA method is enabled. | [optional] [default to False]
**host** | **str** | The server host name or IP address of the MFA provider. | [optional] 
**access_key** | **str** | The secret key for authenticating requests to the MFA provider. | [optional] 
**identity_attribute** | **str** | Optional. The name of the attribute for mapping IdentityNow identity to the MFA provider. | [optional] 
**config_properties** | **Dict[str, object]** | A map with additional config properties for the given MFA method - duo-web. | [optional] 

## Example

```python
from sailpoint.beta.models.mfa_duo_config import MfaDuoConfig

# TODO update the JSON string below
json = "{}"
# create an instance of MfaDuoConfig from a JSON string
mfa_duo_config_instance = MfaDuoConfig.from_json(json)
# print the JSON string representation of the object
print MfaDuoConfig.to_json()

# convert the object into a dict
mfa_duo_config_dict = mfa_duo_config_instance.to_dict()
# create an instance of MfaDuoConfig from a dict
mfa_duo_config_form_dict = mfa_duo_config.from_dict(mfa_duo_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


