# RoleMembershipIdentity

A reference to an Identity in an IDENTITY_LIST role membership criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of the Identity. | [optional] 
**alias_name** | **str** | User name of the Identity | [optional] 

## Example

```python
from sailpoint.v3.models.role_membership_identity import RoleMembershipIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of RoleMembershipIdentity from a JSON string
role_membership_identity_instance = RoleMembershipIdentity.from_json(json)
# print the JSON string representation of the object
print(RoleMembershipIdentity.to_json())

# convert the object into a dict
role_membership_identity_dict = role_membership_identity_instance.to_dict()
# create an instance of RoleMembershipIdentity from a dict
role_membership_identity_from_dict = RoleMembershipIdentity.from_dict(role_membership_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


