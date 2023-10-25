# ListConnectors200ResponseItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_xml** | **str** |  | [optional] 
**class_name** | **str** |  | [optional] 
**connector_metadata** | **object** |  | [optional] 
**correlation_config_xml** | **str** |  | [optional] 
**direct_connect** | **bool** |  | [optional] 
**file_upload** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**s3_location** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**script_name** | **str** |  | [optional] 
**source_config** | **str** |  | [optional] 
**source_config_from** | **str** |  | [optional] 
**source_config_xml** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**translation_properties** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**uploaded_files** | **List[object]** |  | [optional] 

## Example

```python
from cc.models.list_connectors200_response_items_inner import ListConnectors200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectors200ResponseItemsInner from a JSON string
list_connectors200_response_items_inner_instance = ListConnectors200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print ListConnectors200ResponseItemsInner.to_json()

# convert the object into a dict
list_connectors200_response_items_inner_dict = list_connectors200_response_items_inner_instance.to_dict()
# create an instance of ListConnectors200ResponseItemsInner from a dict
list_connectors200_response_items_inner_form_dict = list_connectors200_response_items_inner.from_dict(list_connectors200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


