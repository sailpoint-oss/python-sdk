# SodViolationContextCheckCompleted1

An object referencing a completed SOD violation check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The status of SOD violation check | [optional] 
**uuid** | **str** | The id of the Violation check event | [optional] 
**violation_check_result** | [**SodViolationCheckResult1**](SodViolationCheckResult1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_context_check_completed1 import SodViolationContextCheckCompleted1

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationContextCheckCompleted1 from a JSON string
sod_violation_context_check_completed1_instance = SodViolationContextCheckCompleted1.from_json(json)
# print the JSON string representation of the object
print SodViolationContextCheckCompleted1.to_json()

# convert the object into a dict
sod_violation_context_check_completed1_dict = sod_violation_context_check_completed1_instance.to_dict()
# create an instance of SodViolationContextCheckCompleted1 from a dict
sod_violation_context_check_completed1_form_dict = sod_violation_context_check_completed1.from_dict(sod_violation_context_check_completed1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


