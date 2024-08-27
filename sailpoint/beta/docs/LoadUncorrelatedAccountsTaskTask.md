# LoadUncorrelatedAccountsTaskTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the task this taskStatus represents | [optional] 
**type** | **str** | Type of task this task represents | [optional] 
**name** | **str** | The name of uncorrelated accounts process | [optional] 
**description** | **str** | The description of the task | [optional] 
**launcher** | **str** | The user who initiated the task | [optional] 
**created** | **datetime** | The Task creation date | [optional] 
**launched** | **datetime** | The task start date | [optional] 
**completed** | **datetime** | The task completion date | [optional] 
**completion_status** | **str** | Task completion status. | [optional] 
**parent_name** | **str** | Name of the parent task if exists. | [optional] 
**messages** | [**List[LoadUncorrelatedAccountsTaskTaskMessagesInner]**](LoadUncorrelatedAccountsTaskTaskMessagesInner.md) | List of the messages dedicated to the report.  From task definition perspective here usually should be warnings or errors. | [optional] 
**progress** | **str** | Current task state. | [optional] 
**attributes** | [**LoadUncorrelatedAccountsTaskTaskAttributes**](LoadUncorrelatedAccountsTaskTaskAttributes.md) |  | [optional] 
**returns** | **object** | Return values from the task | [optional] 

## Example

```python
from sailpoint.beta.models.load_uncorrelated_accounts_task_task import LoadUncorrelatedAccountsTaskTask

# TODO update the JSON string below
json = "{}"
# create an instance of LoadUncorrelatedAccountsTaskTask from a JSON string
load_uncorrelated_accounts_task_task_instance = LoadUncorrelatedAccountsTaskTask.from_json(json)
# print the JSON string representation of the object
print(LoadUncorrelatedAccountsTaskTask.to_json())

# convert the object into a dict
load_uncorrelated_accounts_task_task_dict = load_uncorrelated_accounts_task_task_instance.to_dict()
# create an instance of LoadUncorrelatedAccountsTaskTask from a dict
load_uncorrelated_accounts_task_task_from_dict = LoadUncorrelatedAccountsTaskTask.from_dict(load_uncorrelated_accounts_task_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


