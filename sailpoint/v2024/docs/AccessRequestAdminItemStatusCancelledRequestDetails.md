# AccessRequestAdminItemStatusCancelledRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment made by the owner when cancelling the associated request. | [optional] 
**owner** | [**OwnerDto**](OwnerDto.md) |  | [optional] 
**modified** | **datetime** | Date comment was added by the owner when cancelling the associated request. | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_admin_item_status_cancelled_request_details import AccessRequestAdminItemStatusCancelledRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestAdminItemStatusCancelledRequestDetails from a JSON string
access_request_admin_item_status_cancelled_request_details_instance = AccessRequestAdminItemStatusCancelledRequestDetails.from_json(json)
# print the JSON string representation of the object
print(AccessRequestAdminItemStatusCancelledRequestDetails.to_json())

# convert the object into a dict
access_request_admin_item_status_cancelled_request_details_dict = access_request_admin_item_status_cancelled_request_details_instance.to_dict()
# create an instance of AccessRequestAdminItemStatusCancelledRequestDetails from a dict
access_request_admin_item_status_cancelled_request_details_from_dict = AccessRequestAdminItemStatusCancelledRequestDetails.from_dict(access_request_admin_item_status_cancelled_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


