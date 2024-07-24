# Workflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow | [optional] 
**owner** | [**WorkflowBodyOwner**](WorkflowBodyOwner.md) |  | [optional] 
**description** | **str** | Description of what the workflow accomplishes | [optional] 
**definition** | [**WorkflowDefinition**](WorkflowDefinition.md) |  | [optional] 
**enabled** | **bool** | Enable or disable the workflow.  Workflows cannot be created in an enabled state. | [optional] [default to False]
**trigger** | [**WorkflowTrigger**](WorkflowTrigger.md) |  | [optional] 
**id** | **str** | Workflow ID. This is a UUID generated upon creation. | [optional] 
**execution_count** | **int** | The number of times this workflow has been executed. | [optional] 
**failure_count** | **int** | The number of times this workflow has failed during execution. | [optional] 
**created** | **datetime** | The date and time the workflow was created. | [optional] 
**modified** | **datetime** | The date and time the workflow was modified. | [optional] 
**modified_by** | [**WorkflowModifiedBy**](WorkflowModifiedBy.md) |  | [optional] 
**creator** | [**WorkflowAllOfCreator**](WorkflowAllOfCreator.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print Workflow.to_json()

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_form_dict = workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


