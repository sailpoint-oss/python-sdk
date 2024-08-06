# FormDefinitionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique guid identifying the form definition. | [optional] 
**name** | **str** | Name of the form definition. | [optional] 
**description** | **str** | Form definition&#39;s description. | [optional] 
**owner** | [**FormOwner**](FormOwner.md) |  | [optional] 
**used_by** | [**List[FormUsedBy]**](FormUsedBy.md) | List of objects using the form definition. Whenever a system uses a form, the API reaches out to the form service to record that the system is currently using it. | [optional] 
**form_input** | [**List[FormDefinitionInput]**](FormDefinitionInput.md) | List of form inputs required to create a form-instance object. | [optional] 
**form_elements** | [**List[FormElement]**](FormElement.md) | List of nested form elements. | [optional] 
**form_conditions** | [**List[FormCondition]**](FormCondition.md) | Conditional logic that can dynamically modify the form as the recipient is interacting with it. | [optional] 
**created** | **datetime** | Created is the date the form definition was created | [optional] 
**modified** | **datetime** | Modified is the last date the form definition was modified | [optional] 

## Example

```python
from sailpoint.v2024.models.form_definition_response import FormDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionResponse from a JSON string
form_definition_response_instance = FormDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print FormDefinitionResponse.to_json()

# convert the object into a dict
form_definition_response_dict = form_definition_response_instance.to_dict()
# create an instance of FormDefinitionResponse from a dict
form_definition_response_form_dict = form_definition_response.from_dict(form_definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


