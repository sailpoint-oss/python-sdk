# CreateFormDefinitionFileRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | File specifying the multipart | 

## Example

```python
from sailpoint.beta.models.create_form_definition_file_request_request import CreateFormDefinitionFileRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFormDefinitionFileRequestRequest from a JSON string
create_form_definition_file_request_request_instance = CreateFormDefinitionFileRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFormDefinitionFileRequestRequest.to_json())

# convert the object into a dict
create_form_definition_file_request_request_dict = create_form_definition_file_request_request_instance.to_dict()
# create an instance of CreateFormDefinitionFileRequestRequest from a dict
create_form_definition_file_request_request_from_dict = CreateFormDefinitionFileRequestRequest.from_dict(create_form_definition_file_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


