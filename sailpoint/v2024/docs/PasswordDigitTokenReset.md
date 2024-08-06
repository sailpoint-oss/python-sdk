# PasswordDigitTokenReset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The uid of the user requested for digit token | 
**length** | **int** | The length of digit token. It should be from 6 to 18, inclusive. The default value is 6. | [optional] 
**duration_minutes** | **int** | The time to live for the digit token in minutes. The default value is 5 minutes. | [optional] 

## Example

```python
from sailpoint.v2024.models.password_digit_token_reset import PasswordDigitTokenReset

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordDigitTokenReset from a JSON string
password_digit_token_reset_instance = PasswordDigitTokenReset.from_json(json)
# print the JSON string representation of the object
print PasswordDigitTokenReset.to_json()

# convert the object into a dict
password_digit_token_reset_dict = password_digit_token_reset_instance.to_dict()
# create an instance of PasswordDigitTokenReset from a dict
password_digit_token_reset_form_dict = password_digit_token_reset.from_dict(password_digit_token_reset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


