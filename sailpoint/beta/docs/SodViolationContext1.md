# SodViolationContext1

The contextual information of the violated criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**SodPolicyDto**](SodPolicyDto.md) |  | [optional] 
**conflicting_access_criteria** | [**SodViolationContext1ConflictingAccessCriteria**](SodViolationContext1ConflictingAccessCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.sod_violation_context1 import SodViolationContext1

# TODO update the JSON string below
json = "{}"
# create an instance of SodViolationContext1 from a JSON string
sod_violation_context1_instance = SodViolationContext1.from_json(json)
# print the JSON string representation of the object
print(SodViolationContext1.to_json())

# convert the object into a dict
sod_violation_context1_dict = sod_violation_context1_instance.to_dict()
# create an instance of SodViolationContext1 from a dict
sod_violation_context1_from_dict = SodViolationContext1.from_dict(sod_violation_context1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


