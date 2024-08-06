# TranslationMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the translation message | [optional] 
**values** | **List[str]** | The values corresponding to the translation messages | [optional] 

## Example

```python
from sailpoint.v2024.models.translation_message import TranslationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationMessage from a JSON string
translation_message_instance = TranslationMessage.from_json(json)
# print the JSON string representation of the object
print TranslationMessage.to_json()

# convert the object into a dict
translation_message_dict = translation_message_instance.to_dict()
# create an instance of TranslationMessage from a dict
translation_message_form_dict = translation_message.from_dict(translation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


