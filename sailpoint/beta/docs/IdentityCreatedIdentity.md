# IdentityCreatedIdentity

The identity that was created.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.identity_created_identity import IdentityCreatedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCreatedIdentity from a JSON string
identity_created_identity_instance = IdentityCreatedIdentity.from_json(json)
# print the JSON string representation of the object
print IdentityCreatedIdentity.to_json()

# convert the object into a dict
identity_created_identity_dict = identity_created_identity_instance.to_dict()
# create an instance of IdentityCreatedIdentity from a dict
identity_created_identity_form_dict = identity_created_identity.from_dict(identity_created_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


