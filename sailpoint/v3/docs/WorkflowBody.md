# WorkflowBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow | [optional] 
**owner** | [**WorkflowBodyOwner**](WorkflowBodyOwner.md) |  | [optional] 
**description** | **str** | Description of what the workflow accomplishes | [optional] 
**definition** | [**WorkflowDefinition**](WorkflowDefinition.md) |  | [optional] 
**enabled** | **bool** | Enable or disable the workflow.  Workflows cannot be created in an enabled state. | [optional] [default to False]
**trigger** | [**WorkflowTrigger**](WorkflowTrigger.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_body import WorkflowBody

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowBody from a JSON string
workflow_body_instance = WorkflowBody.from_json(json)
# print the JSON string representation of the object
print(WorkflowBody.to_json())

# convert the object into a dict
workflow_body_dict = workflow_body_instance.to_dict()
# create an instance of WorkflowBody from a dict
workflow_body_from_dict = WorkflowBody.from_dict(workflow_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


