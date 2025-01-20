# ApprovalForwardHistory1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_approver_name** | **str** | Display name of approver from whom the approval was forwarded. | [optional] 
**new_approver_name** | **str** | Display name of approver to whom the approval was forwarded. | [optional] 
**comment** | **str** | Comment made while forwarding. | [optional] 
**modified** | **datetime** | Time at which approval was forwarded. | [optional] 
**forwarder_name** | **str** | Display name of forwarder who forwarded the approval. | [optional] 
**reassignment_type** | [**ReassignmentType**](ReassignmentType.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_forward_history1 import ApprovalForwardHistory1

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalForwardHistory1 from a JSON string
approval_forward_history1_instance = ApprovalForwardHistory1.from_json(json)
# print the JSON string representation of the object
print(ApprovalForwardHistory1.to_json())

# convert the object into a dict
approval_forward_history1_dict = approval_forward_history1_instance.to_dict()
# create an instance of ApprovalForwardHistory1 from a dict
approval_forward_history1_from_dict = ApprovalForwardHistory1.from_dict(approval_forward_history1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


