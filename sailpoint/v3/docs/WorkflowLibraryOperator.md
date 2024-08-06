# WorkflowLibraryOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operator ID. | [optional] 
**name** | **str** | Operator friendly name | [optional] 
**type** | **str** | Operator type | [optional] 
**description** | **str** | Description of the operator | [optional] 
**is_dynamic_schema** | **bool** | Determines whether the dynamic output schema is returned in place of the action&#39;s output schema. The dynamic schema lists non-static properties, like properties of a workflow form where each form has different fields. These will be provided dynamically based on available form fields. | [optional] 
**deprecated** | **bool** |  | [optional] 
**deprecated_by** | **datetime** |  | [optional] 
**is_simulation_enabled** | **bool** |  | [optional] 
**form_fields** | [**List[WorkflowLibraryFormFields]**](WorkflowLibraryFormFields.md) | One or more inputs that the operator accepts | [optional] 

## Example

```python
from sailpoint.v3.models.workflow_library_operator import WorkflowLibraryOperator

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLibraryOperator from a JSON string
workflow_library_operator_instance = WorkflowLibraryOperator.from_json(json)
# print the JSON string representation of the object
print WorkflowLibraryOperator.to_json()

# convert the object into a dict
workflow_library_operator_dict = workflow_library_operator_instance.to_dict()
# create an instance of WorkflowLibraryOperator from a dict
workflow_library_operator_form_dict = workflow_library_operator.from_dict(workflow_library_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


