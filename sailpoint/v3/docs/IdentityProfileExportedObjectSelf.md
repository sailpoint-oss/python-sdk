# IdentityProfileExportedObjectSelf

Self block for exported object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Exported object&#39;s DTO type. | [optional] 
**id** | **str** | Exported object&#39;s ID. | [optional] 
**name** | **str** | Exported object&#39;s display name. | [optional] 

## Example

```python
from v3.models.identity_profile_exported_object_self import IdentityProfileExportedObjectSelf

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileExportedObjectSelf from a JSON string
identity_profile_exported_object_self_instance = IdentityProfileExportedObjectSelf.from_json(json)
# print the JSON string representation of the object
print IdentityProfileExportedObjectSelf.to_json()

# convert the object into a dict
identity_profile_exported_object_self_dict = identity_profile_exported_object_self_instance.to_dict()
# create an instance of IdentityProfileExportedObjectSelf from a dict
identity_profile_exported_object_self_form_dict = identity_profile_exported_object_self.from_dict(identity_profile_exported_object_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


