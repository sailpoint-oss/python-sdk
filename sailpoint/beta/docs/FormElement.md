# FormElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** | Config is a config object | [optional] 
**element_type** | **str** | ElementType is a FormElementType value TEXT FormElementTypeText TOGGLE FormElementTypeToggle TEXTAREA FormElementTypeTextArea HIDDEN FormElementTypeHidden PHONE FormElementTypePhone EMAIL FormElementTypeEmail SELECT FormElementTypeSelect DATE FormElementTypeDate SECTION FormElementTypeSection COLUMNS FormElementTypeColumns | [optional] 
**id** | **str** | ID is a form element identifier | [optional] 
**key** | **str** | Key is the technical key | [optional] 
**validations** | **object** | FormElementValidationsSet is a set of FormElementValidation items | [optional] 

## Example

```python
from beta.models.form_element import FormElement

# TODO update the JSON string below
json = "{}"
# create an instance of FormElement from a JSON string
form_element_instance = FormElement.from_json(json)
# print the JSON string representation of the object
print FormElement.to_json()

# convert the object into a dict
form_element_dict = form_element_instance.to_dict()
# create an instance of FormElement from a dict
form_element_form_dict = form_element.from_dict(form_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


