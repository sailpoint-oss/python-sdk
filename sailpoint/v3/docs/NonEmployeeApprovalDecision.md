# NonEmployeeApprovalDecision


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment on the approval item. | [optional] 

## Example

```python
from sailpoint.v3.models.non_employee_approval_decision import NonEmployeeApprovalDecision

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeApprovalDecision from a JSON string
non_employee_approval_decision_instance = NonEmployeeApprovalDecision.from_json(json)
# print the JSON string representation of the object
print NonEmployeeApprovalDecision.to_json()

# convert the object into a dict
non_employee_approval_decision_dict = non_employee_approval_decision_instance.to_dict()
# create an instance of NonEmployeeApprovalDecision from a dict
non_employee_approval_decision_form_dict = non_employee_approval_decision.from_dict(non_employee_approval_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


