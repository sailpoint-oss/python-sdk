# ListWorkgroupConnections200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**object_type** | **str** |  | [optional] 
**workgroup_id** | **str** |  | [optional] 

## Example

```python
from v2.models.list_workgroup_connections200_response_inner import ListWorkgroupConnections200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkgroupConnections200ResponseInner from a JSON string
list_workgroup_connections200_response_inner_instance = ListWorkgroupConnections200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListWorkgroupConnections200ResponseInner.to_json()

# convert the object into a dict
list_workgroup_connections200_response_inner_dict = list_workgroup_connections200_response_inner_instance.to_dict()
# create an instance of ListWorkgroupConnections200ResponseInner from a dict
list_workgroup_connections200_response_inner_form_dict = list_workgroup_connections200_response_inner.from_dict(list_workgroup_connections200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


