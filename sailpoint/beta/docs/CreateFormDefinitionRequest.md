# CreateFormDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is the form definition description | [optional] 
**form_conditions** | [**List[FormCondition]**](FormCondition.md) | FormConditions is the conditional logic that modify the form dynamically modify the form as the recipient is interacting out the form | [optional] 
**form_elements** | [**List[FormElement]**](FormElement.md) | FormElements is a list of nested form elements | [optional] 
**form_input** | [**List[FormDefinitionInput]**](FormDefinitionInput.md) | FormInput is a list of form inputs that are required when creating a form-instance object | [optional] 
**name** | **str** | Name is the form definition name | 
**owner** | [**FormOwner**](FormOwner.md) |  | 
**used_by** | [**List[FormUsedBy]**](FormUsedBy.md) | UsedBy is a list of objects where when any system uses a particular form it reaches out to the form service to record it is currently being used | [optional] 

## Example

```python
from sailpoint.beta.models.create_form_definition_request import CreateFormDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFormDefinitionRequest from a JSON string
create_form_definition_request_instance = CreateFormDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreateFormDefinitionRequest.to_json()

# convert the object into a dict
create_form_definition_request_dict = create_form_definition_request_instance.to_dict()
# create an instance of CreateFormDefinitionRequest from a dict
create_form_definition_request_form_dict = create_form_definition_request.from_dict(create_form_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


