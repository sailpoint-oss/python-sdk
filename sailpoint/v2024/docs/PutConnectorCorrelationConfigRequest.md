# PutConnectorCorrelationConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | connector correlation config xml file | 

## Example

```python
from sailpoint.v2024.models.put_connector_correlation_config_request import PutConnectorCorrelationConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutConnectorCorrelationConfigRequest from a JSON string
put_connector_correlation_config_request_instance = PutConnectorCorrelationConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PutConnectorCorrelationConfigRequest.to_json())

# convert the object into a dict
put_connector_correlation_config_request_dict = put_connector_correlation_config_request_instance.to_dict()
# create an instance of PutConnectorCorrelationConfigRequest from a dict
put_connector_correlation_config_request_from_dict = PutConnectorCorrelationConfigRequest.from_dict(put_connector_correlation_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


