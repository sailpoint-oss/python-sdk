# AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover

The identity of the approver.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of identity who approved the access item request. | 
**name** | **str** | Human-readable display name of identity who approved the access item request. | 

## Example

```python
from beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver import AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover from a JSON string
access_request_post_approval_requested_items_status_inner_approval_info_inner_approver_instance = AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover.from_json(json)
# print the JSON string representation of the object
print AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover.to_json()

# convert the object into a dict
access_request_post_approval_requested_items_status_inner_approval_info_inner_approver_dict = access_request_post_approval_requested_items_status_inner_approval_info_inner_approver_instance.to_dict()
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover from a dict
access_request_post_approval_requested_items_status_inner_approval_info_inner_approver_form_dict = access_request_post_approval_requested_items_status_inner_approval_info_inner_approver.from_dict(access_request_post_approval_requested_items_status_inner_approval_info_inner_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


