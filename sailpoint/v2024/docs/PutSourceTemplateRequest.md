# PutSourceTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector source template xml file | 

## Example

```python
from sailpoint.v2024.models.put_source_template_request import PutSourceTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSourceTemplateRequest from a JSON string
put_source_template_request_instance = PutSourceTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PutSourceTemplateRequest.to_json())

# convert the object into a dict
put_source_template_request_dict = put_source_template_request_instance.to_dict()
# create an instance of PutSourceTemplateRequest from a dict
put_source_template_request_from_dict = PutSourceTemplateRequest.from_dict(put_source_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


