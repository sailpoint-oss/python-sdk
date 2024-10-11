# LauncherRequestReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Launcher reference | 
**id** | **str** | ID of Launcher reference | 

## Example

```python
from sailpoint.beta.models.launcher_request_reference import LauncherRequestReference

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherRequestReference from a JSON string
launcher_request_reference_instance = LauncherRequestReference.from_json(json)
# print the JSON string representation of the object
print(LauncherRequestReference.to_json())

# convert the object into a dict
launcher_request_reference_dict = launcher_request_reference_instance.to_dict()
# create an instance of LauncherRequestReference from a dict
launcher_request_reference_from_dict = LauncherRequestReference.from_dict(launcher_request_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


