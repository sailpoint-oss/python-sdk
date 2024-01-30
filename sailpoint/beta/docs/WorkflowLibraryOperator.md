# WorkflowLibraryOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operator ID. | [optional] 
**name** | **str** | Operator friendly name | [optional] 
**type** | **str** | Operator type | [optional] 
**description** | **str** | Description of the operator | [optional] 
**form_fields** | [**List[WorkflowLibraryFormFields]**](WorkflowLibraryFormFields.md) | One or more inputs that the operator accepts | [optional] 

## Example

```python
from sailpoint.beta.models.workflow_library_operator import WorkflowLibraryOperator

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


