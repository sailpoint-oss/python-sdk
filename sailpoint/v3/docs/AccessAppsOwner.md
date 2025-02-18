# AccessAppsOwner

Owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner&#39;s DTO type. | [optional] 
**id** | **str** | Owner&#39;s identity ID. | [optional] 
**name** | **str** | Owner&#39;s display name. | [optional] 
**email** | **str** | Owner&#39;s email. | [optional] 

## Example

```python
from sailpoint.v3.models.access_apps_owner import AccessAppsOwner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessAppsOwner from a JSON string
access_apps_owner_instance = AccessAppsOwner.from_json(json)
# print the JSON string representation of the object
print(AccessAppsOwner.to_json())

# convert the object into a dict
access_apps_owner_dict = access_apps_owner_instance.to_dict()
# create an instance of AccessAppsOwner from a dict
access_apps_owner_from_dict = AccessAppsOwner.from_dict(access_apps_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


