# ApprovalSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **int** | The number of pending access requests approvals. | [optional] 
**approved** | **int** | The number of approved access requests approvals. | [optional] 
**rejected** | **int** | The number of rejected access requests approvals. | [optional] 

## Example

```python
from v3.models.approval_summary import ApprovalSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalSummary from a JSON string
approval_summary_instance = ApprovalSummary.from_json(json)
# print the JSON string representation of the object
print ApprovalSummary.to_json()

# convert the object into a dict
approval_summary_dict = approval_summary_instance.to_dict()
# create an instance of ApprovalSummary from a dict
approval_summary_form_dict = approval_summary.from_dict(approval_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


