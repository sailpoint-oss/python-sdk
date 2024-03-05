# RequestedItemStatusCancelledRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment made by the owner when cancelling the associated request. | [optional] 
**owner** | [**OwnerDto**](OwnerDto.md) |  | [optional] 
**modified** | **datetime** | Date comment was added by the owner when cancelling the associated request. | [optional] 

## Example

```python
from sailpoint.v3.models.requested_item_status_cancelled_request_details import RequestedItemStatusCancelledRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemStatusCancelledRequestDetails from a JSON string
requested_item_status_cancelled_request_details_instance = RequestedItemStatusCancelledRequestDetails.from_json(json)
# print the JSON string representation of the object
print RequestedItemStatusCancelledRequestDetails.to_json()

# convert the object into a dict
requested_item_status_cancelled_request_details_dict = requested_item_status_cancelled_request_details_instance.to_dict()
# create an instance of RequestedItemStatusCancelledRequestDetails from a dict
requested_item_status_cancelled_request_details_form_dict = requested_item_status_cancelled_request_details.from_dict(requested_item_status_cancelled_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


