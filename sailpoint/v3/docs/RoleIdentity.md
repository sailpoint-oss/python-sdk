# RoleIdentity

A subset of the fields of an Identity which is a member of a Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Identity | [optional] 
**alias_name** | **str** | The alias / username of the Identity | [optional] 
**name** | **str** | The human-readable display name of the Identity | [optional] 
**email** | **str** | Email address of the Identity | [optional] 
**role_assignment_source** | [**RoleAssignmentSourceType**](RoleAssignmentSourceType.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.role_identity import RoleIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of RoleIdentity from a JSON string
role_identity_instance = RoleIdentity.from_json(json)
# print the JSON string representation of the object
print RoleIdentity.to_json()

# convert the object into a dict
role_identity_dict = role_identity_instance.to_dict()
# create an instance of RoleIdentity from a dict
role_identity_form_dict = role_identity.from_dict(role_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


