# ImportConnectorConfigRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | This is the connector config zip bundle which gets uploaded. | [optional] 

## Example

```python
from cc.models.import_connector_config_request import ImportConnectorConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportConnectorConfigRequest from a JSON string
import_connector_config_request_instance = ImportConnectorConfigRequest.from_json(json)
# print the JSON string representation of the object
print ImportConnectorConfigRequest.to_json()

# convert the object into a dict
import_connector_config_request_dict = import_connector_config_request_instance.to_dict()
# create an instance of ImportConnectorConfigRequest from a dict
import_connector_config_request_form_dict = import_connector_config_request.from_dict(import_connector_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


