# AccessRequestPreApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_id** | **str** | The unique ID of the access request. | 
**requested_for** | [**List[AccessItemRequestedForDto]**](AccessItemRequestedForDto.md) | Identities access was requested for. | 
**requested_items** | [**List[AccessRequestPreApprovalRequestedItemsInner]**](AccessRequestPreApprovalRequestedItemsInner.md) | Details of the access items being requested. | 
**requested_by** | [**AccessItemRequesterDto**](AccessItemRequesterDto.md) |  | 

## Example

```python
from sailpoint.v2024.models.access_request_pre_approval import AccessRequestPreApproval

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestPreApproval from a JSON string
access_request_pre_approval_instance = AccessRequestPreApproval.from_json(json)
# print the JSON string representation of the object
print(AccessRequestPreApproval.to_json())

# convert the object into a dict
access_request_pre_approval_dict = access_request_pre_approval_instance.to_dict()
# create an instance of AccessRequestPreApproval from a dict
access_request_pre_approval_from_dict = AccessRequestPreApproval.from_dict(access_request_pre_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


