# LauncherReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of Launcher reference | [optional] 
**id** | **str** | ID of Launcher reference | [optional] 

## Example

```python
from sailpoint.beta.models.launcher_reference import LauncherReference

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherReference from a JSON string
launcher_reference_instance = LauncherReference.from_json(json)
# print the JSON string representation of the object
print(LauncherReference.to_json())

# convert the object into a dict
launcher_reference_dict = launcher_reference_instance.to_dict()
# create an instance of LauncherReference from a dict
launcher_reference_from_dict = LauncherReference.from_dict(launcher_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


