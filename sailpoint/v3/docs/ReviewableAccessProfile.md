# ReviewableAccessProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Access Profile | [optional] 
**name** | **str** | Name of the Access Profile | [optional] 
**description** | **str** | Information about the Access Profile | [optional] 
**privileged** | **bool** | Indicates if the entitlement is a privileged entitlement | [optional] 
**cloud_governed** | **bool** | True if the entitlement is cloud governed | [optional] 
**end_date** | **datetime** | The date at which a user&#39;s access expires | [optional] 
**owner** | [**IdentityReferenceWithNameAndEmail**](IdentityReferenceWithNameAndEmail.md) |  | [optional] 
**entitlements** | [**List[ReviewableEntitlement]**](ReviewableEntitlement.md) | A list of entitlements associated with this Access Profile | [optional] 
**created** | **datetime** | Date the Access Profile was created. | [optional] 
**modified** | **datetime** | Date the Access Profile was last modified. | [optional] 

## Example

```python
from sailpoint.v3.models.reviewable_access_profile import ReviewableAccessProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewableAccessProfile from a JSON string
reviewable_access_profile_instance = ReviewableAccessProfile.from_json(json)
# print the JSON string representation of the object
print(ReviewableAccessProfile.to_json())

# convert the object into a dict
reviewable_access_profile_dict = reviewable_access_profile_instance.to_dict()
# create an instance of ReviewableAccessProfile from a dict
reviewable_access_profile_from_dict = ReviewableAccessProfile.from_dict(reviewable_access_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


