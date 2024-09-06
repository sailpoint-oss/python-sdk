# UserAppSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the source ID | [optional] 
**type** | **str** | It will always be \&quot;SOURCE\&quot; | [optional] 
**name** | **str** | the source name | [optional] 

## Example

```python
from sailpoint.v2024.models.user_app_source import UserAppSource

# TODO update the JSON string below
json = "{}"
# create an instance of UserAppSource from a JSON string
user_app_source_instance = UserAppSource.from_json(json)
# print the JSON string representation of the object
print(UserAppSource.to_json())

# convert the object into a dict
user_app_source_dict = user_app_source_instance.to_dict()
# create an instance of UserAppSource from a dict
user_app_source_from_dict = UserAppSource.from_dict(user_app_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


