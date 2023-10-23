# MfaConfigTestResponse

Response model for configuration test of a given MFA method

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The configuration test result. | [optional] [readonly] 
**error** | **str** | The error message to indicate the failure of configuration test. | [optional] [readonly] 

## Example

```python
from beta.models.mfa_config_test_response import MfaConfigTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MfaConfigTestResponse from a JSON string
mfa_config_test_response_instance = MfaConfigTestResponse.from_json(json)
# print the JSON string representation of the object
print MfaConfigTestResponse.to_json()

# convert the object into a dict
mfa_config_test_response_dict = mfa_config_test_response_instance.to_dict()
# create an instance of MfaConfigTestResponse from a dict
mfa_config_test_response_form_dict = mfa_config_test_response.from_dict(mfa_config_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


