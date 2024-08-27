# PutPasswordDictionaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 

## Example

```python
from sailpoint.beta.models.put_password_dictionary_request import PutPasswordDictionaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPasswordDictionaryRequest from a JSON string
put_password_dictionary_request_instance = PutPasswordDictionaryRequest.from_json(json)
# print the JSON string representation of the object
print(PutPasswordDictionaryRequest.to_json())

# convert the object into a dict
put_password_dictionary_request_dict = put_password_dictionary_request_instance.to_dict()
# create an instance of PutPasswordDictionaryRequest from a dict
put_password_dictionary_request_from_dict = PutPasswordDictionaryRequest.from_dict(put_password_dictionary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


