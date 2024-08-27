# SodPolicySchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | SOD Policy schedule name | [optional] 
**created** | **datetime** | The time when this SOD policy schedule is created. | [optional] [readonly] 
**modified** | **datetime** | The time when this SOD policy schedule is modified. | [optional] [readonly] 
**description** | **str** | SOD Policy schedule description | [optional] 
**schedule** | [**Schedule1**](Schedule1.md) |  | [optional] 
**recipients** | [**List[SodRecipient]**](SodRecipient.md) |  | [optional] 
**email_empty_results** | **bool** | Indicates if empty results need to be emailed | [optional] [default to False]
**creator_id** | **str** | Policy&#39;s creator ID | [optional] [readonly] 
**modifier_id** | **str** | Policy&#39;s modifier ID | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.sod_policy_schedule import SodPolicySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SodPolicySchedule from a JSON string
sod_policy_schedule_instance = SodPolicySchedule.from_json(json)
# print the JSON string representation of the object
print(SodPolicySchedule.to_json())

# convert the object into a dict
sod_policy_schedule_dict = sod_policy_schedule_instance.to_dict()
# create an instance of SodPolicySchedule from a dict
sod_policy_schedule_from_dict = SodPolicySchedule.from_dict(sod_policy_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


