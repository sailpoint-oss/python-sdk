# AccessRequestPostApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_id** | **str** | The unique ID of the access request. | 
**requested_for** | [**List[AccessItemRequestedForDto]**](AccessItemRequestedForDto.md) | Identities access was requested for. | 
**requested_items_status** | [**List[AccessRequestPostApprovalRequestedItemsStatusInner]**](AccessRequestPostApprovalRequestedItemsStatusInner.md) | Details on the outcome of each access item. | 
**requested_by** | [**AccessItemRequesterDto**](AccessItemRequesterDto.md) |  | 

## Example

```python
from sailpoint.v2024.models.access_request_post_approval import AccessRequestPostApproval

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPostApproval from a JSON string
access_request_post_approval_instance = AccessRequestPostApproval.from_json(json)
# print the JSON string representation of the object
print(AccessRequestPostApproval.to_json())

# convert the object into a dict
access_request_post_approval_dict = access_request_post_approval_instance.to_dict()
# create an instance of AccessRequestPostApproval from a dict
access_request_post_approval_from_dict = AccessRequestPostApproval.from_dict(access_request_post_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


