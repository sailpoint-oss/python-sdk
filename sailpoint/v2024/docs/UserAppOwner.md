# UserAppOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID | [optional] 
**type** | **str** | It will always be \&quot;IDENTITY\&quot; | [optional] 
**name** | **str** | The identity name | [optional] 
**alias** | **str** | The identity alias | [optional] 

## Example

```python
from sailpoint.v2024.models.user_app_owner import UserAppOwner

# TODO update the JSON string below
json = "{}"
# create an instance of UserAppOwner from a JSON string
user_app_owner_instance = UserAppOwner.from_json(json)
# print the JSON string representation of the object
print(UserAppOwner.to_json())

# convert the object into a dict
user_app_owner_dict = user_app_owner_instance.to_dict()
# create an instance of UserAppOwner from a dict
user_app_owner_from_dict = UserAppOwner.from_dict(user_app_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


