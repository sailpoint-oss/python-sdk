# TaskDefinitionSummary

Definition of a type of task, used to invoke tasks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the TaskDefinition | 
**unique_name** | **str** | Name of the TaskDefinition | 
**description** | **str** | Description of the TaskDefinition | 
**parent_name** | **str** | Name of the parent of the TaskDefinition | 
**executor** | **str** | Executor of the TaskDefinition | 
**arguments** | **Dict[str, object]** | Formal parameters of the TaskDefinition, without values | 

## Example

```python
from sailpoint.v2024.models.task_definition_summary import TaskDefinitionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDefinitionSummary from a JSON string
task_definition_summary_instance = TaskDefinitionSummary.from_json(json)
# print the JSON string representation of the object
print(TaskDefinitionSummary.to_json())

# convert the object into a dict
task_definition_summary_dict = task_definition_summary_instance.to_dict()
# create an instance of TaskDefinitionSummary from a dict
task_definition_summary_from_dict = TaskDefinitionSummary.from_dict(task_definition_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


