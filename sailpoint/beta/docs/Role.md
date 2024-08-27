# Role

A Role

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Role. This field must be left null when creating an Role, otherwise a 400 Bad Request error will result. | [optional] 
**name** | **str** | The human-readable display name of the Role | 
**created** | **datetime** | Date the Role was created | [optional] [readonly] 
**modified** | **datetime** | Date the Role was last modified. | [optional] [readonly] 
**description** | **str** | A human-readable description of the Role | [optional] 
**owner** | [**OwnerReference**](OwnerReference.md) |  | 
**access_profiles** | [**List[AccessProfileRef]**](AccessProfileRef.md) |  | [optional] 
**entitlements** | [**List[EntitlementRef]**](EntitlementRef.md) |  | [optional] 
**membership** | [**RoleMembershipSelector**](RoleMembershipSelector.md) |  | [optional] 
**legacy_membership_info** | **Dict[str, object]** | This field is not directly modifiable and is generally expected to be *null*. In very rare instances, some Roles may have been created using membership selection criteria that are no longer fully supported. While these Roles will still work, they should be migrated to STANDARD or IDENTITY_LIST selection criteria. This field exists for informational purposes as an aid to such migration. | [optional] 
**enabled** | **bool** | Whether the Role is enabled or not. | [optional] [default to False]
**requestable** | **bool** | Whether the Role can be the target of access requests. | [optional] [default to False]
**access_request_config** | [**RequestabilityForRole**](RequestabilityForRole.md) |  | [optional] 
**revocation_request_config** | [**RevocabilityForRole**](RevocabilityForRole.md) |  | [optional] 
**segments** | **List[str]** | List of IDs of segments, if any, to which this Role is assigned. | [optional] 
**dimensional** | **bool** |  | [optional] 
**dimension_refs** | **str** |  | [optional] 

## Example

```python
from sailpoint.beta.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


