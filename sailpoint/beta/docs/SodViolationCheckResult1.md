# SodViolationCheckResult1

The inner object representing the completed SOD Violation check

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**ErrorMessageDto**](ErrorMessageDto.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on completion of the violation check. | [optional] 
**violation_contexts** | [**List[SodViolationContext1]**](SodViolationContext1.md) |  | [optional] 
**violated_policies** | [**List[SodPolicyDto]**](SodPolicyDto.md) | A list of the Policies that were violated. | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_check_result1 import SodViolationCheckResult1

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationCheckResult1 from a JSON string
sod_violation_check_result1_instance = SodViolationCheckResult1.from_json(json)
# print the JSON string representation of the object
print SodViolationCheckResult1.to_json()

# convert the object into a dict
sod_violation_check_result1_dict = sod_violation_check_result1_instance.to_dict()
# create an instance of SodViolationCheckResult1 from a dict
sod_violation_check_result1_form_dict = sod_violation_check_result1.from_dict(sod_violation_check_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


