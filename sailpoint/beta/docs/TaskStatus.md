# TaskStatus

Details and current status of a specific task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the task this TaskStatus represents | 
**type** | **str** | Type of task this TaskStatus represents | 
**unique_name** | **str** | Name of the task this TaskStatus represents | 
**description** | **str** | Description of the task this TaskStatus represents | 
**parent_name** | **str** | Name of the parent of the task this TaskStatus represents | 
**launcher** | **str** | Service to execute the task this TaskStatus represents | 
**target** | [**Target**](Target.md) |  | [optional] 
**created** | **datetime** | Creation date of the task this TaskStatus represents | 
**modified** | **datetime** | Last modification date of the task this TaskStatus represents | 
**launched** | **datetime** | Launch date of the task this TaskStatus represents | 
**completed** | **datetime** | Completion date of the task this TaskStatus represents | 
**completion_status** | **str** | Completion status of the task this TaskStatus represents | 
**messages** | [**List[TaskStatusMessage]**](TaskStatusMessage.md) | Messages associated with the task this TaskStatus represents | 
**returns** | [**List[TaskReturnDetails]**](TaskReturnDetails.md) | Return values from the task this TaskStatus represents | 
**attributes** | **Dict[str, object]** | Attributes of the task this TaskStatus represents | 
**progress** | **str** | Current progress of the task this TaskStatus represents | 
**percent_complete** | **int** | Current percentage completion of the task this TaskStatus represents | 
**task_definition_summary** | [**TaskDefinitionSummary**](TaskDefinitionSummary.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.task_status import TaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatus from a JSON string
task_status_instance = TaskStatus.from_json(json)
# print the JSON string representation of the object
print TaskStatus.to_json()

# convert the object into a dict
task_status_dict = task_status_instance.to_dict()
# create an instance of TaskStatus from a dict
task_status_form_dict = task_status.from_dict(task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


