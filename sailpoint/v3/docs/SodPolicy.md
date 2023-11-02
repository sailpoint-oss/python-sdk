# SodPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Policy id | [optional] [readonly] 
**name** | **str** | Policy Business Name | [optional] 
**created** | **datetime** | The time when this SOD policy is created. | [optional] [readonly] 
**modified** | **datetime** | The time when this SOD policy is modified. | [optional] [readonly] 
**description** | **str** | Optional description of the SOD policy | [optional] 
**owner_ref** | [**OwnerDto**](OwnerDto.md) |  | [optional] 
**external_policy_reference** | **str** | Optional External Policy Reference | [optional] 
**policy_query** | **str** | Search query of the SOD policy | [optional] 
**compensating_controls** | **str** | Optional compensating controls(Mitigating Controls) | [optional] 
**correction_advice** | **str** | Optional correction advice | [optional] 
**state** | **str** | whether the policy is enforced or not | [optional] 
**tags** | **List[str]** | tags for this policy object | [optional] 
**creator_id** | **str** | Policy&#39;s creator ID | [optional] [readonly] 
**modifier_id** | **str** | Policy&#39;s modifier ID | [optional] [readonly] 
**violation_owner_assignment_config** | [**ViolationOwnerAssignmentConfig**](ViolationOwnerAssignmentConfig.md) |  | [optional] 
**scheduled** | **bool** | defines whether a policy has been scheduled or not | [optional] [default to False]
**type** | **str** | whether a policy is query based or conflicting access based | [optional] [default to 'GENERAL']
**conflicting_access_criteria** | [**SodPolicyConflictingAccessCriteria**](SodPolicyConflictingAccessCriteria.md) |  | [optional] 

## Example

```python
from v3.models.sod_policy import SodPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SodPolicy from a JSON string
sod_policy_instance = SodPolicy.from_json(json)
# print the JSON string representation of the object
print SodPolicy.to_json()

# convert the object into a dict
sod_policy_dict = sod_policy_instance.to_dict()
# create an instance of SodPolicy from a dict
sod_policy_form_dict = sod_policy.from_dict(sod_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


