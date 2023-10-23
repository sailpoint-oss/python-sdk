# IdentityAttributesChangedIdentity

The identity who's attributes changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.identity_attributes_changed_identity import IdentityAttributesChangedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributesChangedIdentity from a JSON string
identity_attributes_changed_identity_instance = IdentityAttributesChangedIdentity.from_json(json)
# print the JSON string representation of the object
print IdentityAttributesChangedIdentity.to_json()

# convert the object into a dict
identity_attributes_changed_identity_dict = identity_attributes_changed_identity_instance.to_dict()
# create an instance of IdentityAttributesChangedIdentity from a dict
identity_attributes_changed_identity_form_dict = identity_attributes_changed_identity.from_dict(identity_attributes_changed_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


