# IdentityCreatedIdentity

Created identity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Created identity&#39;s DTO type. | 
**id** | **str** | Created identity ID. | 
**name** | **str** | Created identity&#39;s display name. | 

## Example

```python
from sailpoint.beta.models.identity_created_identity import IdentityCreatedIdentity

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


