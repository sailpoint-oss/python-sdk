# LauncherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Launcher, limited to 255 characters | 
**description** | **str** | Description of the Launcher, limited to 2000 characters | 
**type** | **str** | Launcher type | 
**disabled** | **bool** | State of the Launcher | 
**reference** | [**LauncherRequestReference**](LauncherRequestReference.md) |  | [optional] 
**config** | **str** | JSON configuration associated with this Launcher, restricted to a max size of 4KB  | 

## Example

```python
from sailpoint.beta.models.launcher_request import LauncherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherRequest from a JSON string
launcher_request_instance = LauncherRequest.from_json(json)
# print the JSON string representation of the object
print(LauncherRequest.to_json())

# convert the object into a dict
launcher_request_dict = launcher_request_instance.to_dict()
# create an instance of LauncherRequest from a dict
launcher_request_from_dict = LauncherRequest.from_dict(launcher_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


