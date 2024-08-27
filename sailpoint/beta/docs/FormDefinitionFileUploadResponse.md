# FormDefinitionFileUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Created is the date the file was uploaded | [optional] 
**file_id** | **str** | fileId is a unique ULID that serves as an identifier for the form definition file | [optional] 
**form_definition_id** | **str** | FormDefinitionID is a unique guid identifying this form definition | [optional] 

## Example

```python
from sailpoint.beta.models.form_definition_file_upload_response import FormDefinitionFileUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionFileUploadResponse from a JSON string
form_definition_file_upload_response_instance = FormDefinitionFileUploadResponse.from_json(json)
# print the JSON string representation of the object
print(FormDefinitionFileUploadResponse.to_json())

# convert the object into a dict
form_definition_file_upload_response_dict = form_definition_file_upload_response_instance.to_dict()
# create an instance of FormDefinitionFileUploadResponse from a dict
form_definition_file_upload_response_from_dict = FormDefinitionFileUploadResponse.from_dict(form_definition_file_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


