# IdentityAttributesChanged


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**IdentityAttributesChangedIdentity**](IdentityAttributesChangedIdentity.md) |  | 
**changes** | [**List[IdentityAttributesChangedChangesInner]**](IdentityAttributesChangedChangesInner.md) | A list of one or more identity attributes that changed on the identity. | 

## Example

```python
from sailpoint.beta.models.identity_attributes_changed import IdentityAttributesChanged

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributesChanged from a JSON string
identity_attributes_changed_instance = IdentityAttributesChanged.from_json(json)
# print the JSON string representation of the object
print IdentityAttributesChanged.to_json()

# convert the object into a dict
identity_attributes_changed_dict = identity_attributes_changed_instance.to_dict()
# create an instance of IdentityAttributesChanged from a dict
identity_attributes_changed_form_dict = identity_attributes_changed.from_dict(identity_attributes_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


