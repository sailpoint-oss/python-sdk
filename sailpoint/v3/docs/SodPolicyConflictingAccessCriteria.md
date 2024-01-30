# SodPolicyConflictingAccessCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_criteria** | [**AccessCriteria**](AccessCriteria.md) |  | [optional] 
**right_criteria** | [**AccessCriteria**](AccessCriteria.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.sod_policy_conflicting_access_criteria import SodPolicyConflictingAccessCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SodPolicyConflictingAccessCriteria from a JSON string
sod_policy_conflicting_access_criteria_instance = SodPolicyConflictingAccessCriteria.from_json(json)
# print the JSON string representation of the object
print SodPolicyConflictingAccessCriteria.to_json()

# convert the object into a dict
sod_policy_conflicting_access_criteria_dict = sod_policy_conflicting_access_criteria_instance.to_dict()
# create an instance of SodPolicyConflictingAccessCriteria from a dict
sod_policy_conflicting_access_criteria_form_dict = sod_policy_conflicting_access_criteria.from_dict(sod_policy_conflicting_access_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


