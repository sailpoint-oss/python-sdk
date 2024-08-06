# CompletedApprovalPreApprovalTriggerResult

If the access request submitted event trigger is configured and this access request was intercepted by it, then this is the result of the trigger's decision to either approve or deny the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The comment from the trigger | [optional] 
**decision** | [**CompletedApprovalState**](CompletedApprovalState.md) |  | [optional] 
**reviewer** | **str** | The name of the approver | [optional] 
**var_date** | **datetime** | The date and time the trigger decided on the request | [optional] 

## Example

```python
from sailpoint.v2024.models.completed_approval_pre_approval_trigger_result import CompletedApprovalPreApprovalTriggerResult

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedApprovalPreApprovalTriggerResult from a JSON string
completed_approval_pre_approval_trigger_result_instance = CompletedApprovalPreApprovalTriggerResult.from_json(json)
# print the JSON string representation of the object
print CompletedApprovalPreApprovalTriggerResult.to_json()

# convert the object into a dict
completed_approval_pre_approval_trigger_result_dict = completed_approval_pre_approval_trigger_result_instance.to_dict()
# create an instance of CompletedApprovalPreApprovalTriggerResult from a dict
completed_approval_pre_approval_trigger_result_form_dict = completed_approval_pre_approval_trigger_result.from_dict(completed_approval_pre_approval_trigger_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


