# WorkflowLibraryAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action ID. This is a static namespaced ID for the action | [optional] 
**name** | **str** | Action Name | [optional] 
**type** | **str** | Action type | [optional] 
**description** | **str** | Action Description | [optional] 
**form_fields** | [**List[WorkflowLibraryFormFields]**](WorkflowLibraryFormFields.md) | One or more inputs that the action accepts | [optional] 
**example_output** | [**WorkflowLibraryActionExampleOutput**](WorkflowLibraryActionExampleOutput.md) |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**deprecated_by** | **datetime** |  | [optional] 
**version_number** | **int** | Version number | [optional] 
**is_simulation_enabled** | **bool** |  | [optional] 
**is_dynamic_schema** | **bool** | Determines whether the dynamic output schema is returned in place of the action&#39;s output schema. The dynamic schema lists non-static properties, like properties of a workflow form where each form has different fields. These will be provided dynamically based on available form fields. | [optional] [default to False]
**output_schema** | **object** | Defines the output schema, if any, that this action produces. | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_library_action import WorkflowLibraryAction

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLibraryAction from a JSON string
workflow_library_action_instance = WorkflowLibraryAction.from_json(json)
# print the JSON string representation of the object
print WorkflowLibraryAction.to_json()

# convert the object into a dict
workflow_library_action_dict = workflow_library_action_instance.to_dict()
# create an instance of WorkflowLibraryAction from a dict
workflow_library_action_form_dict = workflow_library_action.from_dict(workflow_library_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


