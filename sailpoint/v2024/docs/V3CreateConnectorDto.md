# V3CreateConnectorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The connector name. Need to be unique per tenant. The name will able be used to derive a url friendly unique scriptname that will be in response. Script name can then be used for all update endpoints | 
**type** | **str** | The connector type. If not specified will be defaulted to &#39;custom &#39;+name | [optional] 
**class_name** | **str** | The connector class name. If you are implementing openconnector standard (what is recommended), then this need to be set to sailpoint.connector.OpenConnectorAdapter | 
**direct_connect** | **bool** | true if the source is a direct connect source | [optional] [default to True]
**status** | **str** | The connector status | [optional] 

## Example

```python
from sailpoint.v2024.models.v3_create_connector_dto import V3CreateConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of V3CreateConnectorDto from a JSON string
v3_create_connector_dto_instance = V3CreateConnectorDto.from_json(json)
# print the JSON string representation of the object
print V3CreateConnectorDto.to_json()

# convert the object into a dict
v3_create_connector_dto_dict = v3_create_connector_dto_instance.to_dict()
# create an instance of V3CreateConnectorDto from a dict
v3_create_connector_dto_form_dict = v3_create_connector_dto.from_dict(v3_create_connector_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


