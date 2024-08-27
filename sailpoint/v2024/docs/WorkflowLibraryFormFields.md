# WorkflowLibraryFormFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the form field | [optional] 
**help_text** | **str** | Describes the form field in the UI | [optional] 
**label** | **str** | A human readable name for this form field in the UI | [optional] 
**name** | **str** | The name of the input attribute | [optional] 
**required** | **bool** | Denotes if this field is a required attribute | [optional] [default to False]
**type** | **str** | The type of the form field | [optional] 

## Example

```python
from sailpoint.v2024.models.workflow_library_form_fields import WorkflowLibraryFormFields

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowLibraryFormFields from a JSON string
workflow_library_form_fields_instance = WorkflowLibraryFormFields.from_json(json)
# print the JSON string representation of the object
print(WorkflowLibraryFormFields.to_json())

# convert the object into a dict
workflow_library_form_fields_dict = workflow_library_form_fields_instance.to_dict()
# create an instance of WorkflowLibraryFormFields from a dict
workflow_library_form_fields_from_dict = WorkflowLibraryFormFields.from_dict(workflow_library_form_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


