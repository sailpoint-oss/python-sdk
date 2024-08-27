# TaskResultDetails

Details about job or task type, state and lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the job or task underlying in the report processing. It could be a quartz task, QPOC or MENTOS jobs or a refresh/sync task. | [optional] 
**id** | **str** | Unique task definition identifier. | [optional] 
**report_type** | **object** | Use this property to define what report should be processed in the RDE service. | [optional] 
**description** | **str** | Description of the report purpose and/or contents. | [optional] 
**parent_name** | **str** | Name of the parent task/report if exists. | [optional] 
**launcher** | **str** | Name of the report processing initiator. | [optional] 
**created** | **datetime** | Report creation date | [optional] 
**launched** | **datetime** | Report start date | [optional] 
**completed** | **datetime** | Report completion date | [optional] 
**completion_status** | **str** | Report completion status. | [optional] 
**messages** | [**List[TaskResultDetailsMessagesInner]**](TaskResultDetailsMessagesInner.md) | List of the messages dedicated to the report.  From task definition perspective here usually should be warnings or errors. | [optional] 
**returns** | [**List[TaskResultDetailsReturnsInner]**](TaskResultDetailsReturnsInner.md) | Task definition results, if necessary. | [optional] 
**attributes** | **Dict[str, object]** | Extra attributes map(dictionary) needed for the report. | [optional] 
**progress** | **str** | Current report state. | [optional] 

## Example

```python
from sailpoint.v2024.models.task_result_details import TaskResultDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultDetails from a JSON string
task_result_details_instance = TaskResultDetails.from_json(json)
# print the JSON string representation of the object
print(TaskResultDetails.to_json())

# convert the object into a dict
task_result_details_dict = task_result_details_instance.to_dict()
# create an instance of TaskResultDetails from a dict
task_result_details_from_dict = TaskResultDetails.from_dict(task_result_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


