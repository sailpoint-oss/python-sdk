# AccessRequestDynamicApproverRequestedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the access item. | 
**name** | **str** | Human friendly name of the access item. | 
**description** | **str** | Extended description of the access item. | [optional] 
**type** | **object** | The type of access item being requested. | 
**operation** | **object** | Grant or revoke the access item | 
**comment** | **str** | A comment from the requestor on why the access is needed. | [optional] 

## Example

```python
from beta.models.access_request_dynamic_approver_requested_items_inner import AccessRequestDynamicApproverRequestedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestDynamicApproverRequestedItemsInner from a JSON string
access_request_dynamic_approver_requested_items_inner_instance = AccessRequestDynamicApproverRequestedItemsInner.from_json(json)
# print the JSON string representation of the object
print AccessRequestDynamicApproverRequestedItemsInner.to_json()

# convert the object into a dict
access_request_dynamic_approver_requested_items_inner_dict = access_request_dynamic_approver_requested_items_inner_instance.to_dict()
# create an instance of AccessRequestDynamicApproverRequestedItemsInner from a dict
access_request_dynamic_approver_requested_items_inner_form_dict = access_request_dynamic_approver_requested_items_inner.from_dict(access_request_dynamic_approver_requested_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


