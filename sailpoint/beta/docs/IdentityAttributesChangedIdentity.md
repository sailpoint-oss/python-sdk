# IdentityAttributesChangedIdentity

Identity whose attributes changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity whose attributes changed. | 
**id** | **str** | ID of identity whose attributes changed. | 
**name** | **str** | Display name of identity whose attributes changed. | 

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


