# CancelableAccountActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the account activity itself | [optional] 
**name** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**completed** | **datetime** |  | [optional] 
**completion_status** | [**CompletionStatus**](CompletionStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 
**requester_identity_summary** | [**IdentitySummary**](IdentitySummary.md) |  | [optional] 
**target_identity_summary** | [**IdentitySummary**](IdentitySummary.md) |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**items** | [**List[AccountActivityItem]**](AccountActivityItem.md) |  | [optional] 
**execution_status** | [**ExecutionStatus**](ExecutionStatus.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs, if any were included in the corresponding access request | [optional] 
**cancelable** | **bool** | Whether the account activity can be canceled before completion | [optional] 
**cancel_comment** | [**Comment**](Comment.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.cancelable_account_activity import CancelableAccountActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CancelableAccountActivity from a JSON string
cancelable_account_activity_instance = CancelableAccountActivity.from_json(json)
# print the JSON string representation of the object
print CancelableAccountActivity.to_json()

# convert the object into a dict
cancelable_account_activity_dict = cancelable_account_activity_instance.to_dict()
# create an instance of CancelableAccountActivity from a dict
cancelable_account_activity_form_dict = cancelable_account_activity.from_dict(cancelable_account_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


