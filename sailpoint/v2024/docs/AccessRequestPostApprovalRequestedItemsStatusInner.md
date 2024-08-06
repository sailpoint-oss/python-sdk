# AccessRequestPostApprovalRequestedItemsStatusInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the access item being requested. | 
**name** | **str** | The human friendly name of the access item. | 
**description** | **str** | Detailed description of the access item. | [optional] 
**type** | **object** | The type of access item. | 
**operation** | **object** | The action to perform on the access item. | 
**comment** | **str** | A comment from the identity requesting the access. | [optional] 
**client_metadata** | **Dict[str, object]** | Additional customer defined metadata about the access item. | [optional] 
**approval_info** | [**List[AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner]**](AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner.md) | A list of one or more approvers for the access request. | 

## Example

```python
from sailpoint.v2024.models.access_request_post_approval_requested_items_status_inner import AccessRequestPostApprovalRequestedItemsStatusInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInner from a JSON string
access_request_post_approval_requested_items_status_inner_instance = AccessRequestPostApprovalRequestedItemsStatusInner.from_json(json)
# print the JSON string representation of the object
print AccessRequestPostApprovalRequestedItemsStatusInner.to_json()

# convert the object into a dict
access_request_post_approval_requested_items_status_inner_dict = access_request_post_approval_requested_items_status_inner_instance.to_dict()
# create an instance of AccessRequestPostApprovalRequestedItemsStatusInner from a dict
access_request_post_approval_requested_items_status_inner_form_dict = access_request_post_approval_requested_items_status_inner.from_dict(access_request_post_approval_requested_items_status_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


