# UserApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user app id | [optional] 
**created** | **datetime** | Time when the user app was created | [optional] 
**modified** | **datetime** | Time when the user app was last modified | [optional] 
**has_multiple_accounts** | **bool** | True if the owner has multiple accounts for the source | [optional] [default to False]
**use_for_password_management** | **bool** | True if the source has password feature | [optional] [default to False]
**provision_request_enabled** | **bool** | True if the source app related to the user app is provision request enabled | [optional] [default to False]
**app_center_enabled** | **bool** | True if the source app related to the user app is shown in the app center | [optional] [default to True]
**source_app** | [**UserAppSourceApp**](UserAppSourceApp.md) |  | [optional] 
**source** | [**UserAppSource**](UserAppSource.md) |  | [optional] 
**account** | [**UserAppAccount**](UserAppAccount.md) |  | [optional] 
**owner** | [**UserAppOwner**](UserAppOwner.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.user_app import UserApp

# TODO update the JSON string below
json = "{}"
# create an instance of UserApp from a JSON string
user_app_instance = UserApp.from_json(json)
# print the JSON string representation of the object
print(UserApp.to_json())

# convert the object into a dict
user_app_dict = user_app_instance.to_dict()
# create an instance of UserApp from a dict
user_app_from_dict = UserApp.from_dict(user_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


