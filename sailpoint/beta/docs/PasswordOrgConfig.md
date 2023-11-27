# PasswordOrgConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_instructions_enabled** | **bool** | Indicator whether custom password instructions feature is enabled. The default value is false. | [optional] [default to False]
**digit_token_enabled** | **bool** | Indicator whether \&quot;digit token\&quot; feature is enabled. The default value is false. | [optional] [default to False]
**digit_token_duration_minutes** | **int** | The duration of \&quot;digit token\&quot; in minutes. The default value is 5. | [optional] [default to 5]
**digit_token_length** | **int** | The length of \&quot;digit token\&quot;. The default value is 6. | [optional] [default to 6]

## Example

```python
from sailpoint.beta.models.password_org_config import PasswordOrgConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordOrgConfig from a JSON string
password_org_config_instance = PasswordOrgConfig.from_json(json)
# print the JSON string representation of the object
print PasswordOrgConfig.to_json()

# convert the object into a dict
password_org_config_dict = password_org_config_instance.to_dict()
# create an instance of PasswordOrgConfig from a dict
password_org_config_form_dict = password_org_config.from_dict(password_org_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


