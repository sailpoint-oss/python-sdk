# ReviewableEntitlementAccount

Information about the status of the entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**native_identity** | **str** | The native identity for this account | [optional] 
**disabled** | **bool** | Indicates whether this account is currently disabled | [optional] [default to False]
**locked** | **bool** | Indicates whether this account is currently locked | [optional] [default to False]
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | The id associated with the account | [optional] 
**name** | **str** | The account name | [optional] 
**created** | **datetime** | When the account was created | [optional] 
**modified** | **datetime** | When the account was last modified | [optional] 
**activity_insights** | [**ActivityInsights**](ActivityInsights.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.reviewable_entitlement_account import ReviewableEntitlementAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewableEntitlementAccount from a JSON string
reviewable_entitlement_account_instance = ReviewableEntitlementAccount.from_json(json)
# print the JSON string representation of the object
print(ReviewableEntitlementAccount.to_json())

# convert the object into a dict
reviewable_entitlement_account_dict = reviewable_entitlement_account_instance.to_dict()
# create an instance of ReviewableEntitlementAccount from a dict
reviewable_entitlement_account_from_dict = ReviewableEntitlementAccount.from_dict(reviewable_entitlement_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


