# WorkflowExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The workflow execution ID | [optional] 
**workflow_id** | **str** | The workflow ID | [optional] 
**request_id** | **str** | This backend ID tracks a workflow request in the system. You can provide this ID in a customer support ticket for debugging purposes. | [optional] 
**start_time** | **datetime** | The date/time the workflow started | [optional] 
**close_time** | **datetime** | The date/time the workflow ended | [optional] 
**status** | **str** | The workflow execution status | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_execution import WorkflowExecution

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecution from a JSON string
workflow_execution_instance = WorkflowExecution.from_json(json)
# print the JSON string representation of the object
print WorkflowExecution.to_json()

# convert the object into a dict
workflow_execution_dict = workflow_execution_instance.to_dict()
# create an instance of WorkflowExecution from a dict
workflow_execution_form_dict = workflow_execution.from_dict(workflow_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


