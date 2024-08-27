# TaskResultSimplified


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task identifier | [optional] 
**name** | **str** | Task name | [optional] 
**description** | **str** | Task description | [optional] 
**launcher** | **str** | User or process who launched the task | [optional] 
**completed** | **datetime** | Date time of completion | [optional] 
**launched** | **datetime** | Date time when the task was launched | [optional] 
**completion_status** | **str** | Task result status | [optional] 

## Example

```python
from sailpoint.beta.models.task_result_simplified import TaskResultSimplified

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultSimplified from a JSON string
task_result_simplified_instance = TaskResultSimplified.from_json(json)
# print the JSON string representation of the object
print(TaskResultSimplified.to_json())

# convert the object into a dict
task_result_simplified_dict = task_result_simplified_instance.to_dict()
# create an instance of TaskResultSimplified from a dict
task_result_simplified_from_dict = TaskResultSimplified.from_dict(task_result_simplified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


