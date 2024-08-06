# ConnectedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConnectedObjectType**](ConnectedObjectType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable name of Connected object | [optional] 
**description** | **str** | Description of the Connected object. | [optional] 

## Example

```python
from sailpoint.v2024.models.connected_object import ConnectedObject

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedObject from a JSON string
connected_object_instance = ConnectedObject.from_json(json)
# print the JSON string representation of the object
print ConnectedObject.to_json()

# convert the object into a dict
connected_object_dict = connected_object_instance.to_dict()
# create an instance of ConnectedObject from a dict
connected_object_form_dict = connected_object.from_dict(connected_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


