# ApprovalBatch

Batch properties if an approval is sent via batching.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | ID of the batch | [optional] 
**batch_size** | **int** | How many approvals are going to be in this batch. Defaults to 1 if not provided. | [optional] 

## Example

```python
from sailpoint.v2024.models.approval_batch import ApprovalBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalBatch from a JSON string
approval_batch_instance = ApprovalBatch.from_json(json)
# print the JSON string representation of the object
print(ApprovalBatch.to_json())

# convert the object into a dict
approval_batch_dict = approval_batch_instance.to_dict()
# create an instance of ApprovalBatch from a dict
approval_batch_from_dict = ApprovalBatch.from_dict(approval_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


