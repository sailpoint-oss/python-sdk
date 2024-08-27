# ReviewableRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id for the Role | [optional] 
**name** | **str** | The name of the Role | [optional] 
**description** | **str** | Information about the Role | [optional] 
**privileged** | **bool** | Indicates if the entitlement is a privileged entitlement | [optional] 
**owner** | [**IdentityReferenceWithNameAndEmail**](IdentityReferenceWithNameAndEmail.md) |  | [optional] 
**revocable** | **bool** | Indicates whether the Role can be revoked or requested | [optional] 
**end_date** | **datetime** | The date when a user&#39;s access expires. | [optional] 
**access_profiles** | [**List[ReviewableAccessProfile]**](ReviewableAccessProfile.md) | The list of Access Profiles associated with this Role | [optional] 
**entitlements** | [**List[ReviewableEntitlement]**](ReviewableEntitlement.md) | The list of entitlements associated with this Role | [optional] 

## Example

```python
from sailpoint.v2024.models.reviewable_role import ReviewableRole

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewableRole from a JSON string
reviewable_role_instance = ReviewableRole.from_json(json)
# print the JSON string representation of the object
print(ReviewableRole.to_json())

# convert the object into a dict
reviewable_role_dict = reviewable_role_instance.to_dict()
# create an instance of ReviewableRole from a dict
reviewable_role_from_dict = ReviewableRole.from_dict(reviewable_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


