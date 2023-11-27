# PasswordChangeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID that requested the password change | [optional] 
**encrypted_password** | **str** | The RSA encrypted password | [optional] 
**public_key_id** | **str** | The encryption key ID | [optional] 
**account_id** | **str** | Account ID of the account This is specified per account schema in the source configuration. It is used to distinguish accounts. More info can be found here https://community.sailpoint.com/t5/IdentityNow-Connectors/How-do-I-designate-an-account-attribute-as-the-Account-ID-for-a/ta-p/80350 | [optional] 
**source_id** | **str** | The ID of the source for which identity is requesting the password change | [optional] 

## Example

```python
from sailpoint.beta.models.password_change_request import PasswordChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordChangeRequest from a JSON string
password_change_request_instance = PasswordChangeRequest.from_json(json)
# print the JSON string representation of the object
print PasswordChangeRequest.to_json()

# convert the object into a dict
password_change_request_dict = password_change_request_instance.to_dict()
# create an instance of PasswordChangeRequest from a dict
password_change_request_form_dict = password_change_request.from_dict(password_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


