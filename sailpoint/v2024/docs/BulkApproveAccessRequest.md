# BulkApproveAccessRequest

Request body payload for bulk approve access request endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_ids** | **List[str]** | List of approval ids to approve the pending requests | 
**comment** | **str** | Reason for approving the pending access request. | 

## Example

```python
from sailpoint.v2024.models.bulk_approve_access_request import BulkApproveAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkApproveAccessRequest from a JSON string
bulk_approve_access_request_instance = BulkApproveAccessRequest.from_json(json)
# print the JSON string representation of the object
print(BulkApproveAccessRequest.to_json())

# convert the object into a dict
bulk_approve_access_request_dict = bulk_approve_access_request_instance.to_dict()
# create an instance of BulkApproveAccessRequest from a dict
bulk_approve_access_request_from_dict = BulkApproveAccessRequest.from_dict(bulk_approve_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


