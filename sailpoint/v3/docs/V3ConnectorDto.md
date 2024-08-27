# V3ConnectorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The connector name | [optional] 
**type** | **str** | The connector type | [optional] 
**script_name** | **str** | The connector script name | [optional] 
**class_name** | **str** | The connector class name. | [optional] 
**features** | **List[str]** | The list of features supported by the connector | [optional] 
**direct_connect** | **bool** | true if the source is a direct connect source | [optional] [default to False]
**connector_metadata** | **Dict[str, object]** | A map containing metadata pertinent to the connector | [optional] 
**status** | **str** | The connector status | [optional] 

## Example

```python
from sailpoint.v3.models.v3_connector_dto import V3ConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of V3ConnectorDto from a JSON string
v3_connector_dto_instance = V3ConnectorDto.from_json(json)
# print the JSON string representation of the object
print(V3ConnectorDto.to_json())

# convert the object into a dict
v3_connector_dto_dict = v3_connector_dto_instance.to_dict()
# create an instance of V3ConnectorDto from a dict
v3_connector_dto_from_dict = V3ConnectorDto.from_dict(v3_connector_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


