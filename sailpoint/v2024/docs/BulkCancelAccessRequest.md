# BulkCancelAccessRequest

Request body payload for bulk cancel access request endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_ids** | **List[str]** | List of access requests ids to cancel the pending requests | 
**comment** | **str** | Reason for cancelling the pending access request. | 

## Example

```python
from sailpoint.v2024.models.bulk_cancel_access_request import BulkCancelAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCancelAccessRequest from a JSON string
bulk_cancel_access_request_instance = BulkCancelAccessRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCancelAccessRequest.to_json())

# convert the object into a dict
bulk_cancel_access_request_dict = bulk_cancel_access_request_instance.to_dict()
# create an instance of BulkCancelAccessRequest from a dict
bulk_cancel_access_request_from_dict = BulkCancelAccessRequest.from_dict(bulk_cancel_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


