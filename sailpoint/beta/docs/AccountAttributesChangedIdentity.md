# AccountAttributesChangedIdentity

The identity whose account attributes changed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.account_attributes_changed_identity import AccountAttributesChangedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesChangedIdentity from a JSON string
account_attributes_changed_identity_instance = AccountAttributesChangedIdentity.from_json(json)
# print the JSON string representation of the object
print AccountAttributesChangedIdentity.to_json()

# convert the object into a dict
account_attributes_changed_identity_dict = account_attributes_changed_identity_instance.to_dict()
# create an instance of AccountAttributesChangedIdentity from a dict
account_attributes_changed_identity_form_dict = account_attributes_changed_identity.from_dict(account_attributes_changed_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


