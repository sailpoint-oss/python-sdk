# LoadAccountsTaskTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the task this taskStatus represents | [optional] 
**type** | **str** | Type of task this task represents | [optional] 
**name** | **str** | The name of the aggregation process | [optional] 
**description** | **str** | The description of the task | [optional] 
**launcher** | **str** | The user who initiated the task | [optional] 
**created** | **datetime** | The Task creation date | [optional] 
**launched** | **datetime** | The task start date | [optional] 
**completed** | **datetime** | The task completion date | [optional] 
**completion_status** | **str** | Task completion status. | [optional] 
**parent_name** | **str** | Name of the parent task if exists. | [optional] 
**messages** | [**List[LoadAccountsTaskTaskMessagesInner]**](LoadAccountsTaskTaskMessagesInner.md) | List of the messages dedicated to the report.  From task definition perspective here usually should be warnings or errors. | [optional] 
**progress** | **str** | Current task state. | [optional] 
**attributes** | [**LoadAccountsTaskTaskAttributes**](LoadAccountsTaskTaskAttributes.md) |  | [optional] 
**returns** | **object** | Return values from the task | [optional] 

## Example

```python
from sailpoint.beta.models.load_accounts_task_task import LoadAccountsTaskTask

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAccountsTaskTask from a JSON string
load_accounts_task_task_instance = LoadAccountsTaskTask.from_json(json)
# print the JSON string representation of the object
print LoadAccountsTaskTask.to_json()

# convert the object into a dict
load_accounts_task_task_dict = load_accounts_task_task_instance.to_dict()
# create an instance of LoadAccountsTaskTask from a dict
load_accounts_task_task_form_dict = load_accounts_task_task.from_dict(load_accounts_task_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


