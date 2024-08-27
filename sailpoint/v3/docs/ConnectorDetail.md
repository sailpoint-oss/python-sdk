# ConnectorDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The connector name | [optional] 
**type** | **str** | The connector type | [optional] 
**class_name** | **str** | The connector class name | [optional] 
**script_name** | **str** | The connector script name | [optional] 
**application_xml** | **str** | The connector application xml | [optional] 
**correlation_config_xml** | **str** | The connector correlation config xml | [optional] 
**source_config_xml** | **str** | The connector source config xml | [optional] 
**source_config** | **str** | The connector source config | [optional] 
**source_config_from** | **str** | The connector source config origin | [optional] 
**s3_location** | **str** | storage path key for this connector | [optional] 
**uploaded_files** | **List[str]** | The list of uploaded files supported by the connector. If there was any executable files uploaded to thee connector. Typically this be empty as the executable be uploaded at source creation. | [optional] 
**file_upload** | **bool** | true if the source is file upload | [optional] [default to False]
**direct_connect** | **bool** | true if the source is a direct connect source | [optional] [default to False]
**translation_properties** | **Dict[str, object]** | A map containing translation attributes by loacale key | [optional] 
**connector_metadata** | **Dict[str, object]** | A map containing metadata pertinent to the UI to be used | [optional] 
**status** | **str** | The connector status | [optional] 

## Example

```python
from sailpoint.v3.models.connector_detail import ConnectorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorDetail from a JSON string
connector_detail_instance = ConnectorDetail.from_json(json)
# print the JSON string representation of the object
print(ConnectorDetail.to_json())

# convert the object into a dict
connector_detail_dict = connector_detail_instance.to_dict()
# create an instance of ConnectorDetail from a dict
connector_detail_from_dict = ConnectorDetail.from_dict(connector_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


