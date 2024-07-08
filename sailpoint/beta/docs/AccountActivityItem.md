# AccountActivityItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Item id | [optional] 
**name** | **str** | Human-readable display name of item | [optional] 
**requested** | **datetime** | Date and time item was requested | [optional] 
**approval_status** | [**AccountActivityApprovalStatus**](AccountActivityApprovalStatus.md) |  | [optional] 
**provisioning_status** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**requester_comment** | [**Comment**](Comment.md) |  | [optional] 
**reviewer_identity_summary** | [**IdentitySummary**](IdentitySummary.md) |  | [optional] 
**reviewer_comment** | [**Comment**](Comment.md) |  | [optional] 
**operation** | [**AccountActivityItemOperation**](AccountActivityItemOperation.md) |  | [optional] 
**attribute** | **str** | Attribute to which account activity applies | [optional] 
**value** | **str** | Value of attribute | [optional] 
**native_identity** | **str** | Native identity in the target system to which the account activity applies | [optional] 
**source_id** | **str** | Id of Source to which account activity applies | [optional] 
**account_request_info** | [**AccountRequestInfo**](AccountRequestInfo.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs, if any were included in the corresponding access request item | [optional] 
**remove_date** | **datetime** | The date the role or access profile or entitlement is no longer assigned to the specified identity. | [optional] 

## Example

```python
from sailpoint.beta.models.account_activity_item import AccountActivityItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivityItem from a JSON string
account_activity_item_instance = AccountActivityItem.from_json(json)
# print the JSON string representation of the object
print AccountActivityItem.to_json()

# convert the object into a dict
account_activity_item_dict = account_activity_item_instance.to_dict()
# create an instance of AccountActivityItem from a dict
account_activity_item_form_dict = account_activity_item.from_dict(account_activity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


