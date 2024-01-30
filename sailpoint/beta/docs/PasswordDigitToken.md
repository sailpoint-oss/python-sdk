# PasswordDigitToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digit_token** | **str** | The digit token for password management | [optional] 
**request_id** | **str** | The reference ID of the digit token generation request | [optional] 

## Example

```python
from sailpoint.beta.models.password_digit_token import PasswordDigitToken

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordDigitToken from a JSON string
password_digit_token_instance = PasswordDigitToken.from_json(json)
# print the JSON string representation of the object
print PasswordDigitToken.to_json()

# convert the object into a dict
password_digit_token_dict = password_digit_token_instance.to_dict()
# create an instance of PasswordDigitToken from a dict
password_digit_token_form_dict = password_digit_token.from_dict(password_digit_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


