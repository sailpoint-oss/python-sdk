# WorkflowExecutionEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of event | [optional] 
**timestamp** | **datetime** | The date-time when the event occurred | [optional] 
**attributes** | **object** | Additional attributes associated with the event | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_execution_event import WorkflowExecutionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionEvent from a JSON string
workflow_execution_event_instance = WorkflowExecutionEvent.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecutionEvent.to_json())

# convert the object into a dict
workflow_execution_event_dict = workflow_execution_event_instance.to_dict()
# create an instance of WorkflowExecutionEvent from a dict
workflow_execution_event_from_dict = WorkflowExecutionEvent.from_dict(workflow_execution_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


