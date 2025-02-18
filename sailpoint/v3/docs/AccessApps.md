# AccessApps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | Name of application | [optional] 
**description** | **str** | Description of application. | [optional] 
**owner** | [**AccessAppsOwner**](AccessAppsOwner.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.access_apps import AccessApps

# TODO update the JSON string below
json = "{}"
# create an instance of AccessApps from a JSON string
access_apps_instance = AccessApps.from_json(json)
# print the JSON string representation of the object
print(AccessApps.to_json())

# convert the object into a dict
access_apps_dict = access_apps_instance.to_dict()
# create an instance of AccessApps from a dict
access_apps_from_dict = AccessApps.from_dict(access_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


