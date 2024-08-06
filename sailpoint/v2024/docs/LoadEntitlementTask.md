# LoadEntitlementTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the task this taskStatus represents | [optional] 
**type** | **str** | Type of task this task represents | [optional] 
**unique_name** | **str** | The name of the task | [optional] 
**description** | **str** | The description of the task | [optional] 
**launcher** | **str** | The user who initiated the task | [optional] 
**created** | **datetime** | The creation date of the task | [optional] 
**returns** | [**List[LoadEntitlementTaskReturnsInner]**](LoadEntitlementTaskReturnsInner.md) | Return values from the task | [optional] 

## Example

```python
from sailpoint.v2024.models.load_entitlement_task import LoadEntitlementTask

# TODO update the JSON string below
json = "{}"
# create an instance of LoadEntitlementTask from a JSON string
load_entitlement_task_instance = LoadEntitlementTask.from_json(json)
# print the JSON string representation of the object
print LoadEntitlementTask.to_json()

# convert the object into a dict
load_entitlement_task_dict = load_entitlement_task_instance.to_dict()
# create an instance of LoadEntitlementTask from a dict
load_entitlement_task_form_dict = load_entitlement_task.from_dict(load_entitlement_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


