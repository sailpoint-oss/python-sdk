# PasswordInfoAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account ID of the account. This is specified per account schema in the source configuration. It is used to distinguish accounts. More info can be found here https://community.sailpoint.com/t5/IdentityNow-Connectors/How-do-I-designate-an-account-attribute-as-the-Account-ID-for-a/ta-p/80350 | [optional] 
**account_name** | **str** | Display name of the account. This is specified per account schema in the source configuration. It is used to display name of the account. More info can be found here https://community.sailpoint.com/t5/IdentityNow-Connectors/How-do-I-designate-an-account-attribute-as-the-Account-Name-for/ta-p/74008 | [optional] 

## Example

```python
from sailpoint.beta.models.password_info_account import PasswordInfoAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordInfoAccount from a JSON string
password_info_account_instance = PasswordInfoAccount.from_json(json)
# print the JSON string representation of the object
print PasswordInfoAccount.to_json()

# convert the object into a dict
password_info_account_dict = password_info_account_instance.to_dict()
# create an instance of PasswordInfoAccount from a dict
password_info_account_form_dict = password_info_account.from_dict(password_info_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


