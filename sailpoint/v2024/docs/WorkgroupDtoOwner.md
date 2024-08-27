# WorkgroupDtoOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Owner&#39;s DTO type. | [optional] 
**id** | **str** | Owner&#39;s identity ID. | [optional] 
**name** | **str** | Owner&#39;s name. | [optional] 
**display_name** | **str** | The display name of the identity | [optional] [readonly] 
**email_address** | **str** | The primary email address of the identity | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.workgroup_dto_owner import WorkgroupDtoOwner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupDtoOwner from a JSON string
workgroup_dto_owner_instance = WorkgroupDtoOwner.from_json(json)
# print the JSON string representation of the object
print(WorkgroupDtoOwner.to_json())

# convert the object into a dict
workgroup_dto_owner_dict = workgroup_dto_owner_instance.to_dict()
# create an instance of WorkgroupDtoOwner from a dict
workgroup_dto_owner_from_dict = WorkgroupDtoOwner.from_dict(workgroup_dto_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


