# WorkgroupConnectionDtoObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConnectedObjectType**](ConnectedObjectType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable name of Connected object | [optional] 
**description** | **str** | Description of the Connected object. | [optional] 

## Example

```python
from sailpoint.v2024.models.workgroup_connection_dto_object import WorkgroupConnectionDtoObject

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupConnectionDtoObject from a JSON string
workgroup_connection_dto_object_instance = WorkgroupConnectionDtoObject.from_json(json)
# print the JSON string representation of the object
print(WorkgroupConnectionDtoObject.to_json())

# convert the object into a dict
workgroup_connection_dto_object_dict = workgroup_connection_dto_object_instance.to_dict()
# create an instance of WorkgroupConnectionDtoObject from a dict
workgroup_connection_dto_object_from_dict = WorkgroupConnectionDtoObject.from_dict(workgroup_connection_dto_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


