# WorkgroupConnectionDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ConnectedObject**](ConnectedObject.md) |  | [optional] 
**connection_type** | **str** | Connection Type. | [optional] 

## Example

```python
from beta.models.workgroup_connection_dto import WorkgroupConnectionDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupConnectionDto from a JSON string
workgroup_connection_dto_instance = WorkgroupConnectionDto.from_json(json)
# print the JSON string representation of the object
print WorkgroupConnectionDto.to_json()

# convert the object into a dict
workgroup_connection_dto_dict = workgroup_connection_dto_instance.to_dict()
# create an instance of WorkgroupConnectionDto from a dict
workgroup_connection_dto_form_dict = workgroup_connection_dto.from_dict(workgroup_connection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


