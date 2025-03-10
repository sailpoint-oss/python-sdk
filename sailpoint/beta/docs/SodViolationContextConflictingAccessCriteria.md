# SodViolationContextConflictingAccessCriteria

The object which contains the left and right hand side of the entitlements that got violated according to the policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_criteria** | [**SodViolationContextConflictingAccessCriteriaLeftCriteria**](SodViolationContextConflictingAccessCriteriaLeftCriteria.md) |  | [optional] 
**right_criteria** | [**SodViolationContextConflictingAccessCriteriaLeftCriteria**](SodViolationContextConflictingAccessCriteriaLeftCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_context_conflicting_access_criteria import SodViolationContextConflictingAccessCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationContextConflictingAccessCriteria from a JSON string
sod_violation_context_conflicting_access_criteria_instance = SodViolationContextConflictingAccessCriteria.from_json(json)
# print the JSON string representation of the object
print(SodViolationContextConflictingAccessCriteria.to_json())

# convert the object into a dict
sod_violation_context_conflicting_access_criteria_dict = sod_violation_context_conflicting_access_criteria_instance.to_dict()
# create an instance of SodViolationContextConflictingAccessCriteria from a dict
sod_violation_context_conflicting_access_criteria_from_dict = SodViolationContextConflictingAccessCriteria.from_dict(sod_violation_context_conflicting_access_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


