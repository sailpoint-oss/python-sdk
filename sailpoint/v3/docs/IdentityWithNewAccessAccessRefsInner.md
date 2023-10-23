# IdentityWithNewAccessAccessRefsInner

The types of objects supported for SOD violations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from v3.models.identity_with_new_access_access_refs_inner import IdentityWithNewAccessAccessRefsInner

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


