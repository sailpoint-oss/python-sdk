# PutConnectorSourceTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector source template xml file | 

## Example

```python
from sailpoint.v3.models.put_connector_source_template_request import PutConnectorSourceTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutConnectorSourceTemplateRequest from a JSON string
put_connector_source_template_request_instance = PutConnectorSourceTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PutConnectorSourceTemplateRequest.to_json())

# convert the object into a dict
put_connector_source_template_request_dict = put_connector_source_template_request_instance.to_dict()
# create an instance of PutConnectorSourceTemplateRequest from a dict
put_connector_source_template_request_from_dict = PutConnectorSourceTemplateRequest.from_dict(put_connector_source_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


