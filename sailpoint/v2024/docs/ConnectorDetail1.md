# ConnectorDetail1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The connector name | [optional] 
**source_config_xml** | **str** | XML representation of the source config data | [optional] 
**source_config** | **str** | JSON representation of the source config data | [optional] 
**direct_connect** | **bool** | true if the source is a direct connect source | [optional] 
**file_upload** | **bool** | Connector config&#39;s file upload attribute, false if not there | [optional] 
**uploaded_files** | **str** | List of uploaded file strings for the connector | [optional] 
**connector_metadata** | **object** | Object containing metadata pertinent to the UI to be used | [optional] 

## Example

```python
from sailpoint.v2024.models.connector_detail1 import ConnectorDetail1

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorDetail1 from a JSON string
connector_detail1_instance = ConnectorDetail1.from_json(json)
# print the JSON string representation of the object
print(ConnectorDetail1.to_json())

# convert the object into a dict
connector_detail1_dict = connector_detail1_instance.to_dict()
# create an instance of ConnectorDetail1 from a dict
connector_detail1_from_dict = ConnectorDetail1.from_dict(connector_detail1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


