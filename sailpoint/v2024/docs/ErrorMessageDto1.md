# ErrorMessageDto1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The locale for the message text, a BCP 47 language tag. | [optional] 
**locale_origin** | [**LocaleOrigin**](LocaleOrigin.md) |  | [optional] 
**text** | **str** | Actual text of the error message in the indicated locale. | [optional] 

## Example

```python
from sailpoint.v2024.models.error_message_dto1 import ErrorMessageDto1

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessageDto1 from a JSON string
error_message_dto1_instance = ErrorMessageDto1.from_json(json)
# print the JSON string representation of the object
print(ErrorMessageDto1.to_json())

# convert the object into a dict
error_message_dto1_dict = error_message_dto1_instance.to_dict()
# create an instance of ErrorMessageDto1 from a dict
error_message_dto1_from_dict = ErrorMessageDto1.from_dict(error_message_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


