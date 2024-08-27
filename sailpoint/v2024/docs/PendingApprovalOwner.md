# PendingApprovalOwner

Access item owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Access item owner&#39;s DTO type. | [optional] 
**id** | **str** | Access item owner&#39;s identity ID. | [optional] 
**name** | **str** | Access item owner&#39;s human-readable display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.pending_approval_owner import PendingApprovalOwner

# TODO update the JSON string below
json = "{}"
# create an instance of PendingApprovalOwner from a JSON string
pending_approval_owner_instance = PendingApprovalOwner.from_json(json)
# print the JSON string representation of the object
print(PendingApprovalOwner.to_json())

# convert the object into a dict
pending_approval_owner_dict = pending_approval_owner_instance.to_dict()
# create an instance of PendingApprovalOwner from a dict
pending_approval_owner_from_dict = PendingApprovalOwner.from_dict(pending_approval_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


