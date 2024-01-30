# WorkflowDefinition

The map of steps that the workflow will execute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **str** | The name of the starting step. | [optional] 
**steps** | **Dict[str, object]** | One or more step objects that comprise this workflow.  Please see the Workflow documentation to see the JSON schema for each step type. | [optional] 

## Example

```python
from sailpoint.beta.models.workflow_definition import WorkflowDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowDefinition from a JSON string
workflow_definition_instance = WorkflowDefinition.from_json(json)
# print the JSON string representation of the object
print WorkflowDefinition.to_json()

# convert the object into a dict
workflow_definition_dict = workflow_definition_instance.to_dict()
# create an instance of WorkflowDefinition from a dict
workflow_definition_form_dict = workflow_definition.from_dict(workflow_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


