# FormElementValidationsSet

Set of FormElementValidation items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_type** | **str** | The type of data validation that you wish to enforce, e.g., a required field, a minimum length, etc. | [optional] 

## Example

```python
from sailpoint.beta.models.form_element_validations_set import FormElementValidationsSet

# TODO update the JSON string below
json = "{}"
# create an instance of FormElementValidationsSet from a JSON string
form_element_validations_set_instance = FormElementValidationsSet.from_json(json)
# print the JSON string representation of the object
print(FormElementValidationsSet.to_json())

# convert the object into a dict
form_element_validations_set_dict = form_element_validations_set_instance.to_dict()
# create an instance of FormElementValidationsSet from a dict
form_element_validations_set_from_dict = FormElementValidationsSet.from_dict(form_element_validations_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


