# AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_comment** | **str** | A comment left by the approver. | [optional] 
**approval_decision** | **object** | The final decision of the approver. | 
**approver_name** | **str** | The name of the approver | 
**approver** | [**AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover**](AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover.md) |  | 

## Example

```python
from sailpoint.v2024.models.access_request_post_approval_requested_items_status_inner_approval_info_inner import AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner from a JSON string
access_request_post_approval_requested_items_status_inner_approval_info_inner_instance = AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner.from_json(json)
# print the JSON string representation of the object
print AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner.to_json()

# convert the object into a dict
access_request_post_approval_requested_items_status_inner_approval_info_inner_dict = access_request_post_approval_requested_items_status_inner_approval_info_inner_instance.to_dict()
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner from a dict
access_request_post_approval_requested_items_status_inner_approval_info_inner_form_dict = access_request_post_approval_requested_items_status_inner_approval_info_inner.from_dict(access_request_post_approval_requested_items_status_inner_approval_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


