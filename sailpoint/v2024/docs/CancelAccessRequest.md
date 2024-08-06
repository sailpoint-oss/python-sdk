# CancelAccessRequest

Request body payload for cancel access request endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_activity_id** | **str** | This refers to the identityRequestId. To successfully cancel an access request, you must provide the identityRequestId. | 
**comment** | **str** | Reason for cancelling the pending access request. | 

## Example

```python
from sailpoint.v2024.models.cancel_access_request import CancelAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelAccessRequest from a JSON string
cancel_access_request_instance = CancelAccessRequest.from_json(json)
# print the JSON string representation of the object
print CancelAccessRequest.to_json()

# convert the object into a dict
cancel_access_request_dict = cancel_access_request_instance.to_dict()
# create an instance of CancelAccessRequest from a dict
cancel_access_request_form_dict = cancel_access_request.from_dict(cancel_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


