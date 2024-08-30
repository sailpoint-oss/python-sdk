# UserAppAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the account ID | [optional] 
**type** | **str** | It will always be \&quot;ACCOUNT\&quot; | [optional] 
**name** | **str** | the account name | [optional] 

## Example

```python
from sailpoint.beta.models.user_app_account import UserAppAccount

# TODO update the JSON string below
json = "{}"
# create an instance of UserAppAccount from a JSON string
user_app_account_instance = UserAppAccount.from_json(json)
# print the JSON string representation of the object
print(UserAppAccount.to_json())

# convert the object into a dict
user_app_account_dict = user_app_account_instance.to_dict()
# create an instance of UserAppAccount from a dict
user_app_account_from_dict = UserAppAccount.from_dict(user_app_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


