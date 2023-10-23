# SodViolationCheckResult

The inner object representing the completed SOD Violation check

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**ErrorMessageDto**](ErrorMessageDto.md) |  | [optional] 
**client_metadata** | **Dict[str, str]** | Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on completion of the violation check. | [optional] 
**violation_contexts** | [**List[SodViolationContext]**](SodViolationContext.md) |  | [optional] 
**violated_policies** | [**List[BaseReferenceDto1]**](BaseReferenceDto1.md) | A list of the Policies that were violated | [optional] 

## Example

```python
from beta.models.sod_violation_check_result import SodViolationCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationCheckResult from a JSON string
sod_violation_check_result_instance = SodViolationCheckResult.from_json(json)
# print the JSON string representation of the object
print SodViolationCheckResult.to_json()

# convert the object into a dict
sod_violation_check_result_dict = sod_violation_check_result_instance.to_dict()
# create an instance of SodViolationCheckResult from a dict
sod_violation_check_result_form_dict = sod_violation_check_result.from_dict(sod_violation_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


