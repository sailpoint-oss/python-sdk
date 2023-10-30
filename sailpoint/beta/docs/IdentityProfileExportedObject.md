# IdentityProfileExportedObject

Identity Profile exported object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version or object from the target service. | [optional] 
**var_self** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 
**object** | [**IdentityProfile1**](IdentityProfile1.md) |  | [optional] 

## Example

```python
from beta.models.identity_profile_exported_object import IdentityProfileExportedObject

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProfileExportedObject from a JSON string
identity_profile_exported_object_instance = IdentityProfileExportedObject.from_json(json)
# print the JSON string representation of the object
print IdentityProfileExportedObject.to_json()

# convert the object into a dict
identity_profile_exported_object_dict = identity_profile_exported_object_instance.to_dict()
# create an instance of IdentityProfileExportedObject from a dict
identity_profile_exported_object_form_dict = identity_profile_exported_object.from_dict(identity_profile_exported_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


