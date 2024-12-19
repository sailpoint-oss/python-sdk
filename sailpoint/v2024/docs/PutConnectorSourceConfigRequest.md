# PutConnectorSourceConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector source config xml file | 

## Example

```python
from sailpoint.v2024.models.put_connector_source_config_request import PutConnectorSourceConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutConnectorSourceConfigRequest from a JSON string
put_connector_source_config_request_instance = PutConnectorSourceConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PutConnectorSourceConfigRequest.to_json())

# convert the object into a dict
put_connector_source_config_request_dict = put_connector_source_config_request_instance.to_dict()
# create an instance of PutConnectorSourceConfigRequest from a dict
put_connector_source_config_request_from_dict = PutConnectorSourceConfigRequest.from_dict(put_connector_source_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


