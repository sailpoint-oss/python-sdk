# PreviewDataSourceResponse

PreviewDataSourceResponse is the response sent by /form-definitions/{formDefinitionID}/data-source endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FormElementDataSourceConfigOptions]**](FormElementDataSourceConfigOptions.md) | Results holds a list of FormElementDataSourceConfigOptions items | [optional] 

## Example

```python
from beta.models.preview_data_source_response import PreviewDataSourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewDataSourceResponse from a JSON string
preview_data_source_response_instance = PreviewDataSourceResponse.from_json(json)
# print the JSON string representation of the object
print PreviewDataSourceResponse.to_json()

# convert the object into a dict
preview_data_source_response_dict = preview_data_source_response_instance.to_dict()
# create an instance of PreviewDataSourceResponse from a dict
preview_data_source_response_form_dict = preview_data_source_response.from_dict(preview_data_source_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


