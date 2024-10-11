# Launcher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the Launcher | 
**created** | **datetime** | Date the Launcher was created | 
**modified** | **datetime** | Date the Launcher was last modified | 
**owner** | [**LauncherOwner**](LauncherOwner.md) |  | 
**name** | **str** | Name of the Launcher, limited to 255 characters | 
**description** | **str** | Description of the Launcher, limited to 2000 characters | 
**type** | **str** | Launcher type | 
**disabled** | **bool** | State of the Launcher | 
**reference** | [**LauncherReference**](LauncherReference.md) |  | [optional] 
**config** | **str** | JSON configuration associated with this Launcher, restricted to a max size of 4KB  | 

## Example

```python
from sailpoint.beta.models.launcher import Launcher

# TODO update the JSON string below
json = "{}"
# create an instance of Launcher from a JSON string
launcher_instance = Launcher.from_json(json)
# print the JSON string representation of the object
print(Launcher.to_json())

# convert the object into a dict
launcher_dict = launcher_instance.to_dict()
# create an instance of Launcher from a dict
launcher_from_dict = Launcher.from_dict(launcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


