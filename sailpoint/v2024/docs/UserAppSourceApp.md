# UserAppSourceApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the source app ID | [optional] 
**type** | **str** | It will always be \&quot;APPLICATION\&quot; | [optional] 
**name** | **str** | the source app name | [optional] 

## Example

```python
from sailpoint.v2024.models.user_app_source_app import UserAppSourceApp

# TODO update the JSON string below
json = "{}"
# create an instance of UserAppSourceApp from a JSON string
user_app_source_app_instance = UserAppSourceApp.from_json(json)
# print the JSON string representation of the object
print(UserAppSourceApp.to_json())

# convert the object into a dict
user_app_source_app_dict = user_app_source_app_instance.to_dict()
# create an instance of UserAppSourceApp from a dict
user_app_source_app_from_dict = UserAppSourceApp.from_dict(user_app_source_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


