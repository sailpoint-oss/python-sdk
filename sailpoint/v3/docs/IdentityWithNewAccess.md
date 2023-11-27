# IdentityWithNewAccess

An identity with a set of access to be added

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | Identity id to be checked. | 
**access_refs** | [**List[IdentityWithNewAccessAccessRefsInner]**](IdentityWithNewAccessAccessRefsInner.md) | The list of entitlements to consider for possible violations in a preventive check. | 

## Example

```python
from sailpoint.v3.models.identity_with_new_access import IdentityWithNewAccess

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityWithNewAccess from a JSON string
identity_with_new_access_instance = IdentityWithNewAccess.from_json(json)
# print the JSON string representation of the object
print IdentityWithNewAccess.to_json()

# convert the object into a dict
identity_with_new_access_dict = identity_with_new_access_instance.to_dict()
# create an instance of IdentityWithNewAccess from a dict
identity_with_new_access_form_dict = identity_with_new_access.from_dict(identity_with_new_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


