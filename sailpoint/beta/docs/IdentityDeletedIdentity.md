# IdentityDeletedIdentity

The identity that was deleted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.identity_deleted_identity import IdentityDeletedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityDeletedIdentity from a JSON string
identity_deleted_identity_instance = IdentityDeletedIdentity.from_json(json)
# print the JSON string representation of the object
print IdentityDeletedIdentity.to_json()

# convert the object into a dict
identity_deleted_identity_dict = identity_deleted_identity_instance.to_dict()
# create an instance of IdentityDeletedIdentity from a dict
identity_deleted_identity_form_dict = identity_deleted_identity.from_dict(identity_deleted_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


