# RequestedItemStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable display name of the item being requested. | [optional] 
**type** | **str** | Type of requested object. | [optional] 
**cancelled_request_details** | [**CancelledRequestDetails**](CancelledRequestDetails.md) |  | [optional] 
**error_messages** | **List[List[ErrorMessageDto]]** | List of list of localized error messages, if any, encountered during the approval/provisioning process. | [optional] 
**state** | [**RequestedItemStatusRequestState**](RequestedItemStatusRequestState.md) |  | [optional] 
**approval_details** | [**List[ApprovalStatusDto]**](ApprovalStatusDto.md) | Approval details for each item. | [optional] 
**manual_work_item_details** | [**List[ManualWorkItemDetails]**](ManualWorkItemDetails.md) | Manual work items created for provisioning the item. | [optional] 
**account_activity_item_id** | **str** | Id of associated account activity item. | [optional] 
**request_type** | [**AccessRequestType**](AccessRequestType.md) |  | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 
**requester** | [**BaseReferenceDto1**](BaseReferenceDto1.md) |  | [optional] 
**requested_for** | [**BaseReferenceDto1**](BaseReferenceDto1.md) |  | [optional] 
**requester_comment** | [**CommentDto1**](CommentDto1.md) |  | [optional] 
**sod_violation_context** | [**SodViolationContextCheckCompleted**](SodViolationContextCheckCompleted.md) |  | [optional] 
**provisioning_details** | [**ProvisioningDetails**](ProvisioningDetails.md) |  | [optional] 
**pre_approval_trigger_details** | [**PreApprovalTriggerDetails**](PreApprovalTriggerDetails.md) |  | [optional] 
**access_request_phases** | [**List[AccessRequestPhases]**](AccessRequestPhases.md) | A list of Phases that the Access Request has gone through in order, to help determine the status of the request. | [optional] 
**description** | **str** | Description associated to the requested object. | [optional] 
**remove_date** | **datetime** | When the role access is scheduled for removal. | [optional] 
**cancelable** | **bool** | True if the request can be canceled. | [optional] 
**access_request_id** | **str** | This is the account activity id. | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs, if any were included in the corresponding access request | [optional] 

## Example

```python
from beta.models.requested_item_status import RequestedItemStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatus from a JSON string
requested_item_status_instance = RequestedItemStatus.from_json(json)
# print the JSON string representation of the object
print RequestedItemStatus.to_json()

# convert the object into a dict
requested_item_status_dict = requested_item_status_instance.to_dict()
# create an instance of RequestedItemStatus from a dict
requested_item_status_form_dict = requested_item_status.from_dict(requested_item_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


