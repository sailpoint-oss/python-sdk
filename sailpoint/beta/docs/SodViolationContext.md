# SodViolationContext

The contextual information of the violated criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**SodPolicyDto**](SodPolicyDto.md) |  | [optional] 
**conflicting_access_criteria** | [**SodViolationContextConflictingAccessCriteria**](SodViolationContextConflictingAccessCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_context import SodViolationContext

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationContext from a JSON string
sod_violation_context_instance = SodViolationContext.from_json(json)
# print the JSON string representation of the object
print SodViolationContext.to_json()

# convert the object into a dict
sod_violation_context_dict = sod_violation_context_instance.to_dict()
# create an instance of SodViolationContext from a dict
sod_violation_context_form_dict = sod_violation_context.from_dict(sod_violation_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


