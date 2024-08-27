# AccountAttributesChangedIdentity

The identity whose account attributes were updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of the identity whose account attributes were updated. | 
**id** | **str** | ID of the identity whose account attributes were updated. | 
**name** | **str** | Display name of the identity whose account attributes were updated. | 

## Example

```python
from sailpoint.beta.models.account_attributes_changed_identity import AccountAttributesChangedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesChangedIdentity from a JSON string
account_attributes_changed_identity_instance = AccountAttributesChangedIdentity.from_json(json)
# print the JSON string representation of the object
print(AccountAttributesChangedIdentity.to_json())

# convert the object into a dict
account_attributes_changed_identity_dict = account_attributes_changed_identity_instance.to_dict()
# create an instance of AccountAttributesChangedIdentity from a dict
account_attributes_changed_identity_from_dict = AccountAttributesChangedIdentity.from_dict(account_attributes_changed_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


