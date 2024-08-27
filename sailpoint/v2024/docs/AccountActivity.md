# AccountActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the account activity | [optional] 
**name** | **str** | The name of the activity | [optional] 
**created** | **datetime** | When the activity was first created | [optional] 
**modified** | **datetime** | When the activity was last modified | [optional] 
**completed** | **datetime** | When the activity was completed | [optional] 
**completion_status** | [**CompletionStatus**](CompletionStatus.md) |  | [optional] 
**type** | **str** | The type of action the activity performed.  Please see the following list of types.  This list may grow over time.  - CloudAutomated - IdentityAttributeUpdate - appRequest - LifecycleStateChange - AccountStateUpdate - AccountAttributeUpdate - CloudPasswordRequest - Attribute Synchronization Refresh - Certification - Identity Refresh - Lifecycle Change Refresh   [Learn more here](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html#searching-account-activity-data).  | [optional] 
**requester_identity_summary** | [**IdentitySummary**](IdentitySummary.md) |  | [optional] 
**target_identity_summary** | [**IdentitySummary**](IdentitySummary.md) |  | [optional] 
**errors** | **List[str]** | A list of error messages, if any, that were encountered. | [optional] 
**warnings** | **List[str]** | A list of warning messages, if any, that were encountered. | [optional] 
**items** | [**List[AccountActivityItem]**](AccountActivityItem.md) | Individual actions performed as part of this account activity | [optional] 
**execution_status** | [**ExecutionStatus**](ExecutionStatus.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs, if any were included in the corresponding access request | [optional] 

## Example

```python
from sailpoint.v2024.models.account_activity import AccountActivity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivity from a JSON string
account_activity_instance = AccountActivity.from_json(json)
# print the JSON string representation of the object
print(AccountActivity.to_json())

# convert the object into a dict
account_activity_dict = account_activity_instance.to_dict()
# create an instance of AccountActivity from a dict
account_activity_from_dict = AccountActivity.from_dict(account_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


