# UpdatePasswordDictionaryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 

## Example

```python
from sailpoint.beta.models.update_password_dictionary_request import UpdatePasswordDictionaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordDictionaryRequest from a JSON string
update_password_dictionary_request_instance = UpdatePasswordDictionaryRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordDictionaryRequest.to_json()

# convert the object into a dict
update_password_dictionary_request_dict = update_password_dictionary_request_instance.to_dict()
# create an instance of UpdatePasswordDictionaryRequest from a dict
update_password_dictionary_request_form_dict = update_password_dictionary_request.from_dict(update_password_dictionary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


