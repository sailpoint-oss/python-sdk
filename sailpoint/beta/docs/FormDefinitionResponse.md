# FormDefinitionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Created is the date the form definition was created | [optional] 
**description** | **str** | Description is the form definition description | [optional] 
**form_conditions** | [**List[FormCondition]**](FormCondition.md) | FormConditions is the conditional logic that modify the form dynamically modify the form as the recipient is interacting out the form | [optional] 
**form_elements** | [**List[FormElement]**](FormElement.md) | FormElements is a list of nested form elements | [optional] 
**form_input** | [**List[FormDefinitionInput]**](FormDefinitionInput.md) | FormInput is a list of form inputs that are required when creating a form-instance object | [optional] 
**id** | **str** | FormDefinitionID is a unique guid identifying this form definition | [optional] 
**modified** | **datetime** | Modified is the last date the form definition was modified | [optional] 
**name** | **str** | Name is the form definition name | [optional] 
**owner** | [**FormOwner**](FormOwner.md) |  | [optional] 
**used_by** | [**List[FormUsedBy]**](FormUsedBy.md) | UsedBy is a list of objects where when any system uses a particular form it reaches out to the form service to record it is currently being used | [optional] 

## Example

```python
from beta.models.form_definition_response import FormDefinitionResponse

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


