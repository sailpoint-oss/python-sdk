# WorkflowLibraryTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Trigger ID. This is a static namespaced ID for the trigger. | [optional] 
**type** | **str** | Trigger type | [optional] 
**deprecated** | **bool** |  | [optional] 
**deprecated_by** | **datetime** |  | [optional] 
**is_simulation_enabled** | **bool** |  | [optional] 
**output_schema** | **object** | Example output schema | [optional] 
**name** | **str** | Trigger Name | [optional] 
**description** | **str** | Trigger Description | [optional] 
**is_dynamic_schema** | **bool** | Determines whether the dynamic output schema is returned in place of the action&#39;s output schema. The dynamic schema lists non-static properties, like properties of a workflow form where each form has different fields. These will be provided dynamically based on available form fields. | [optional] [default to False]
**input_example** | **object** | Example trigger payload if applicable | [optional] 
**form_fields** | [**List[WorkflowLibraryFormFields]**](WorkflowLibraryFormFields.md) | One or more inputs that the trigger accepts | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_library_trigger import WorkflowLibraryTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLibraryTrigger from a JSON string
workflow_library_trigger_instance = WorkflowLibraryTrigger.from_json(json)
# print the JSON string representation of the object
print(WorkflowLibraryTrigger.to_json())

# convert the object into a dict
workflow_library_trigger_dict = workflow_library_trigger_instance.to_dict()
# create an instance of WorkflowLibraryTrigger from a dict
workflow_library_trigger_from_dict = WorkflowLibraryTrigger.from_dict(workflow_library_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


