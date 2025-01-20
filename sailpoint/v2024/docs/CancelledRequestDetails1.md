# CancelledRequestDetails1

Provides additional details for a request that has been cancelled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment made by the owner when cancelling the associated request. | [optional] 
**owner** | [**OwnerDto**](OwnerDto.md) |  | [optional] 
**modified** | **datetime** | Date comment was added by the owner when cancelling the associated request. | [optional] 

## Example

```python
from sailpoint.v2024.models.cancelled_request_details1 import CancelledRequestDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledRequestDetails1 from a JSON string
cancelled_request_details1_instance = CancelledRequestDetails1.from_json(json)
# print the JSON string representation of the object
print(CancelledRequestDetails1.to_json())

# convert the object into a dict
cancelled_request_details1_dict = cancelled_request_details1_instance.to_dict()
# create an instance of CancelledRequestDetails1 from a dict
cancelled_request_details1_from_dict = CancelledRequestDetails1.from_dict(cancelled_request_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


