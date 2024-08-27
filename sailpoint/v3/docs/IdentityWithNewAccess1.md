# IdentityWithNewAccess1

An identity with a set of access to be added

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | Set of identity IDs to be checked. | 
**access_refs** | [**List[EntitlementRef1]**](EntitlementRef1.md) | The bundle of access profiles to be added to the identities specified. All references must be ENTITLEMENT type. | 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on completion of the violation check. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_with_new_access1 import IdentityWithNewAccess1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityWithNewAccess1 from a JSON string
identity_with_new_access1_instance = IdentityWithNewAccess1.from_json(json)
# print the JSON string representation of the object
print(IdentityWithNewAccess1.to_json())

# convert the object into a dict
identity_with_new_access1_dict = identity_with_new_access1_instance.to_dict()
# create an instance of IdentityWithNewAccess1 from a dict
identity_with_new_access1_from_dict = IdentityWithNewAccess1.from_dict(identity_with_new_access1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


