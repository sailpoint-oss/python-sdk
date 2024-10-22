# ReviewableEntitlementAccountOwner

Information about the machine account owner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id associated with the machine account owner | [optional] 
**type** | **str** | An enumeration of the types of Owner supported within the IdentityNow infrastructure. | [optional] 
**display_name** | **str** | The machine account owner&#39;s display name | [optional] 

## Example

```python
from sailpoint.v3.models.reviewable_entitlement_account_owner import ReviewableEntitlementAccountOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewableEntitlementAccountOwner from a JSON string
reviewable_entitlement_account_owner_instance = ReviewableEntitlementAccountOwner.from_json(json)
# print the JSON string representation of the object
print(ReviewableEntitlementAccountOwner.to_json())

# convert the object into a dict
reviewable_entitlement_account_owner_dict = reviewable_entitlement_account_owner_instance.to_dict()
# create an instance of ReviewableEntitlementAccountOwner from a dict
reviewable_entitlement_account_owner_from_dict = ReviewableEntitlementAccountOwner.from_dict(reviewable_entitlement_account_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


