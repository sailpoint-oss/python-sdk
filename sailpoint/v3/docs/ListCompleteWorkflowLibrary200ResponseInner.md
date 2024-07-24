# ListCompleteWorkflowLibrary200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operator ID. | [optional] 
**name** | **str** | Operator friendly name | [optional] 
**type** | **str** | Operator type | [optional] 
**description** | **str** | Description of the operator | [optional] 
**form_fields** | [**List[WorkflowLibraryFormFields]**](WorkflowLibraryFormFields.md) | One or more inputs that the operator accepts | [optional] 
**example_output** | [**WorkflowLibraryActionExampleOutput**](WorkflowLibraryActionExampleOutput.md) |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**deprecated_by** | **datetime** |  | [optional] 
**version_number** | **int** | Version number | [optional] 
**is_simulation_enabled** | **bool** |  | [optional] 
**is_dynamic_schema** | **bool** | Determines whether the dynamic output schema is returned in place of the action&#39;s output schema. The dynamic schema lists non-static properties, like properties of a workflow form where each form has different fields. These will be provided dynamically based on available form fields. | [optional] 
**output_schema** | **object** | Example output schema | [optional] 
**input_example** | **object** | Example trigger payload if applicable | [optional] 

## Example

```python
from sailpoint.v3.models.list_complete_workflow_library200_response_inner import ListCompleteWorkflowLibrary200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompleteWorkflowLibrary200ResponseInner from a JSON string
list_complete_workflow_library200_response_inner_instance = ListCompleteWorkflowLibrary200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListCompleteWorkflowLibrary200ResponseInner.to_json()

# convert the object into a dict
list_complete_workflow_library200_response_inner_dict = list_complete_workflow_library200_response_inner_instance.to_dict()
# create an instance of ListCompleteWorkflowLibrary200ResponseInner from a dict
list_complete_workflow_library200_response_inner_form_dict = list_complete_workflow_library200_response_inner.from_dict(list_complete_workflow_library200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


