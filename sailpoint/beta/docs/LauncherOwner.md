# LauncherOwner

Owner of the Launcher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner type | 
**id** | **str** | Owner ID | 

## Example

```python
from sailpoint.beta.models.launcher_owner import LauncherOwner

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherOwner from a JSON string
launcher_owner_instance = LauncherOwner.from_json(json)
# print the JSON string representation of the object
print(LauncherOwner.to_json())

# convert the object into a dict
launcher_owner_dict = launcher_owner_instance.to_dict()
# create an instance of LauncherOwner from a dict
launcher_owner_from_dict = LauncherOwner.from_dict(launcher_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


