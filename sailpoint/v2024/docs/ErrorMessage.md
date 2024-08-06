# ErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Locale is the current Locale | [optional] 
**locale_origin** | **str** | LocaleOrigin holds possible values of how the locale was selected | [optional] 
**text** | **str** | Text is the actual text of the error message | [optional] 

## Example

```python
from sailpoint.v2024.models.error_message import ErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessage from a JSON string
error_message_instance = ErrorMessage.from_json(json)
# print the JSON string representation of the object
print ErrorMessage.to_json()

# convert the object into a dict
error_message_dict = error_message_instance.to_dict()
# create an instance of ErrorMessage from a dict
error_message_form_dict = error_message.from_dict(error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


