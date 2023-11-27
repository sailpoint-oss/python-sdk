# SodViolationContextCheckCompleted

An object referencing a completed SOD violation check

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The status of SOD violation check | [optional] 
**uuid** | **str** | The id of the Violation check event | [optional] 
**violation_check_result** | [**SodViolationCheckResult**](SodViolationCheckResult.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_context_check_completed import SodViolationContextCheckCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationContextCheckCompleted from a JSON string
sod_violation_context_check_completed_instance = SodViolationContextCheckCompleted.from_json(json)
# print the JSON string representation of the object
print SodViolationContextCheckCompleted.to_json()

# convert the object into a dict
sod_violation_context_check_completed_dict = sod_violation_context_check_completed_instance.to_dict()
# create an instance of SodViolationContextCheckCompleted from a dict
sod_violation_context_check_completed_form_dict = sod_violation_context_check_completed.from_dict(sod_violation_context_check_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


