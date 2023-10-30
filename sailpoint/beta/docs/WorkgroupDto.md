# WorkgroupDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | [**BaseReferenceDto**](BaseReferenceDto.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] [readonly] 
**name** | **str** | Name of the Governance Group | [optional] 
**description** | **str** | Description of the Governance Group | [optional] 
**member_count** | **int** | Number of members in the Governance Group. | [optional] [readonly] 
**connection_count** | **int** | Number of connections in the Governance Group. | [optional] [readonly] 

## Example

```python
from beta.models.workgroup_dto import WorkgroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupDto from a JSON string
workgroup_dto_instance = WorkgroupDto.from_json(json)
# print the JSON string representation of the object
print WorkgroupDto.to_json()

# convert the object into a dict
workgroup_dto_dict = workgroup_dto_instance.to_dict()
# create an instance of WorkgroupDto from a dict
workgroup_dto_form_dict = workgroup_dto.from_dict(workgroup_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


