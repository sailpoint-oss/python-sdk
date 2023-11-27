# FormError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key is the technical key | [optional] 
**messages** | [**List[ErrorMessage]**](ErrorMessage.md) | Messages is a list of web.ErrorMessage items | [optional] 
**value** | **object** | Value is the value associated with a Key | [optional] 

## Example

```python
from sailpoint.beta.models.form_error import FormError

# TODO update the JSON string below
json = "{}"
# create an instance of FormError from a JSON string
form_error_instance = FormError.from_json(json)
# print the JSON string representation of the object
print FormError.to_json()

# convert the object into a dict
form_error_dict = form_error_instance.to_dict()
# create an instance of FormError from a dict
form_error_form_dict = form_error.from_dict(form_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


