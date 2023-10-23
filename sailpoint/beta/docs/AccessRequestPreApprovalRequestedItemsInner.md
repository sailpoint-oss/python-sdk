# AccessRequestPreApprovalRequestedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the access item being requested. | 
**name** | **str** | The human friendly name of the access item. | 
**description** | **str** | Detailed description of the access item. | [optional] 
**type** | **object** | The type of access item. | 
**operation** | **object** | The action to perform on the access item. | 
**comment** | **str** | A comment from the identity requesting the access. | [optional] 

## Example

```python
from beta.models.access_request_pre_approval_requested_items_inner import AccessRequestPreApprovalRequestedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPreApprovalRequestedItemsInner from a JSON string
access_request_pre_approval_requested_items_inner_instance = AccessRequestPreApprovalRequestedItemsInner.from_json(json)
# print the JSON string representation of the object
print AccessRequestPreApprovalRequestedItemsInner.to_json()

# convert the object into a dict
access_request_pre_approval_requested_items_inner_dict = access_request_pre_approval_requested_items_inner_instance.to_dict()
# create an instance of AccessRequestPreApprovalRequestedItemsInner from a dict
access_request_pre_approval_requested_items_inner_form_dict = access_request_pre_approval_requested_items_inner.from_dict(access_request_pre_approval_requested_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


