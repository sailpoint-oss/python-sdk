# CreateWorkflowRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow | 
**owner** | [**WorkflowBodyOwner**](WorkflowBodyOwner.md) |  | 
**description** | **str** | Description of what the workflow accomplishes | [optional] 
**definition** | [**WorkflowDefinition**](WorkflowDefinition.md) |  | [optional] 
**enabled** | **bool** | Enable or disable the workflow.  Workflows cannot be created in an enabled state. | [optional] [default to False]
**trigger** | [**WorkflowTrigger**](WorkflowTrigger.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.create_workflow_request import CreateWorkflowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflowRequest from a JSON string
create_workflow_request_instance = CreateWorkflowRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkflowRequest.to_json())

# convert the object into a dict
create_workflow_request_dict = create_workflow_request_instance.to_dict()
# create an instance of CreateWorkflowRequest from a dict
create_workflow_request_from_dict = CreateWorkflowRequest.from_dict(create_workflow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


