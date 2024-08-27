# FormElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Form element identifier. | [optional] 
**element_type** | **str** | FormElementType value.  TEXT FormElementTypeText TOGGLE FormElementTypeToggle TEXTAREA FormElementTypeTextArea HIDDEN FormElementTypeHidden PHONE FormElementTypePhone EMAIL FormElementTypeEmail SELECT FormElementTypeSelect DATE FormElementTypeDate SECTION FormElementTypeSection COLUMN_SET FormElementTypeColumns IMAGE FormElementTypeImage DESCRIPTION FormElementTypeDescription | [optional] 
**config** | **Dict[str, object]** | Config object. | [optional] 
**key** | **str** | Technical key. | [optional] 
**validations** | [**List[FormElementValidationsSet]**](FormElementValidationsSet.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.form_element import FormElement

# TODO update the JSON string below
json = "{}"
# create an instance of FormElement from a JSON string
form_element_instance = FormElement.from_json(json)
# print the JSON string representation of the object
print(FormElement.to_json())

# convert the object into a dict
form_element_dict = form_element_instance.to_dict()
# create an instance of FormElement from a dict
form_element_from_dict = FormElement.from_dict(form_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


