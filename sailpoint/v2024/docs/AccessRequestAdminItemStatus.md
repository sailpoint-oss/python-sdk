# AccessRequestAdminItemStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the access request. This is a new property as of 2025. Older access requests may not have an ID. | [optional] 
**name** | **str** | Human-readable display name of the item being requested. | [optional] 
**type** | **str** | Type of requested object. | [optional] 
**cancelled_request_details** | [**RequestedItemStatusCancelledRequestDetails**](RequestedItemStatusCancelledRequestDetails.md) |  | [optional] 
**error_messages** | **List[List[ErrorMessageDto]]** | List of localized error messages, if any, encountered during the approval/provisioning process. | [optional] 
**state** | [**RequestedItemStatusRequestState**](RequestedItemStatusRequestState.md) |  | [optional] 
**approval_details** | [**List[ApprovalStatusDto]**](ApprovalStatusDto.md) | Approval details for each item. | [optional] 
**manual_work_item_details** | [**List[ManualWorkItemDetails]**](ManualWorkItemDetails.md) | Manual work items created for provisioning the item. | [optional] 
**account_activity_item_id** | **str** | Id of associated account activity item. | [optional] 
**request_type** | [**AccessRequestType**](AccessRequestType.md) |  | [optional] 
**modified** | **datetime** | When the request was last modified. | [optional] 
**created** | **datetime** | When the request was created. | [optional] 
**requester** | [**AccessItemRequester**](AccessItemRequester.md) |  | [optional] 
**requested_for** | [**RequestedItemStatusRequestedFor**](RequestedItemStatusRequestedFor.md) |  | [optional] 
**requester_comment** | [**RequestedItemStatusRequesterComment**](RequestedItemStatusRequesterComment.md) |  | [optional] 
**sod_violation_context** | [**RequestedItemStatusSodViolationContext**](RequestedItemStatusSodViolationContext.md) |  | [optional] 
**provisioning_details** | [**RequestedItemStatusProvisioningDetails**](RequestedItemStatusProvisioningDetails.md) |  | [optional] 
**pre_approval_trigger_details** | [**RequestedItemStatusPreApprovalTriggerDetails**](RequestedItemStatusPreApprovalTriggerDetails.md) |  | [optional] 
**access_request_phases** | [**List[AccessRequestPhases]**](AccessRequestPhases.md) | A list of Phases that the Access Request has gone through in order, to help determine the status of the request. | [optional] 
**description** | **str** | Description associated to the requested object. | [optional] 
**remove_date** | **datetime** | When the role access is scheduled for removal. | [optional] 
**cancelable** | **bool** | True if the request can be canceled. | [optional] [default to False]
**reauthorization_required** | **bool** | True if re-auth is required. | [optional] [default to False]
**access_request_id** | **str** | This is the account activity id. | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs, if any were included in the corresponding access request | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_admin_item_status import AccessRequestAdminItemStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestAdminItemStatus from a JSON string
access_request_admin_item_status_instance = AccessRequestAdminItemStatus.from_json(json)
# print the JSON string representation of the object
print(AccessRequestAdminItemStatus.to_json())

# convert the object into a dict
access_request_admin_item_status_dict = access_request_admin_item_status_instance.to_dict()
# create an instance of AccessRequestAdminItemStatus from a dict
access_request_admin_item_status_from_dict = AccessRequestAdminItemStatus.from_dict(access_request_admin_item_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


