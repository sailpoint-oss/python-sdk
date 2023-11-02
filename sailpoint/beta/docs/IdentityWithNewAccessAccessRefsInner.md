# IdentityWithNewAccessAccessRefsInner

Entitlement including a specific set of access.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entitlement&#39;s DTO type. | [optional] 
**id** | **str** | Entitlement&#39;s ID. | [optional] 
**name** | **str** | Entitlement&#39;s display name. | [optional] 

## Example

```python
from beta.models.identity_with_new_access_access_refs_inner import IdentityWithNewAccessAccessRefsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityWithNewAccessAccessRefsInner from a JSON string
identity_with_new_access_access_refs_inner_instance = IdentityWithNewAccessAccessRefsInner.from_json(json)
# print the JSON string representation of the object
print IdentityWithNewAccessAccessRefsInner.to_json()

# convert the object into a dict
identity_with_new_access_access_refs_inner_dict = identity_with_new_access_access_refs_inner_instance.to_dict()
# create an instance of IdentityWithNewAccessAccessRefsInner from a dict
identity_with_new_access_access_refs_inner_form_dict = identity_with_new_access_access_refs_inner.from_dict(identity_with_new_access_access_refs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


