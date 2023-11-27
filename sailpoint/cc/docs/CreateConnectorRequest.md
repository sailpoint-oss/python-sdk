# CreateConnectorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**class_name** | **str** |  | [optional] 
**direct_connect** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sailpoint.cc.models.create_connector_request import CreateConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectorRequest from a JSON string
create_connector_request_instance = CreateConnectorRequest.from_json(json)
# print the JSON string representation of the object
print CreateConnectorRequest.to_json()

# convert the object into a dict
create_connector_request_dict = create_connector_request_instance.to_dict()
# create an instance of CreateConnectorRequest from a dict
create_connector_request_form_dict = create_connector_request.from_dict(create_connector_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


