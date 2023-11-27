# FormDefinitionInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the form input. | [optional] 
**type** | **str** | FormDefinitionInputType value. STRING FormDefinitionInputTypeString | [optional] 
**label** | **str** | Name for the form input. | [optional] 
**description** | **str** | Form input&#39;s description. | [optional] 

## Example

```python
from sailpoint.beta.models.form_definition_input import FormDefinitionInput

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionInput from a JSON string
form_definition_input_instance = FormDefinitionInput.from_json(json)
# print the JSON string representation of the object
print FormDefinitionInput.to_json()

# convert the object into a dict
form_definition_input_dict = form_definition_input_instance.to_dict()
# create an instance of FormDefinitionInput from a dict
form_definition_input_form_dict = form_definition_input.from_dict(form_definition_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


