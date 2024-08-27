# FormElementPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | [**FormElementDynamicDataSource**](FormElementDynamicDataSource.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.form_element_preview_request import FormElementPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormElementPreviewRequest from a JSON string
form_element_preview_request_instance = FormElementPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(FormElementPreviewRequest.to_json())

# convert the object into a dict
form_element_preview_request_dict = form_element_preview_request_instance.to_dict()
# create an instance of FormElementPreviewRequest from a dict
form_element_preview_request_from_dict = FormElementPreviewRequest.from_dict(form_element_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


