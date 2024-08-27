# ListWorkgroupMembers200ResponseInner

Identity of workgroup member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Workgroup member identity DTO type. | [optional] 
**id** | **str** | Workgroup member identity ID. | [optional] 
**name** | **str** | Workgroup member identity display name. | [optional] 
**email** | **str** | Workgroup member identity email. | [optional] 

## Example

```python
from sailpoint.v2024.models.list_workgroup_members200_response_inner import ListWorkgroupMembers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWorkgroupMembers200ResponseInner from a JSON string
list_workgroup_members200_response_inner_instance = ListWorkgroupMembers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListWorkgroupMembers200ResponseInner.to_json())

# convert the object into a dict
list_workgroup_members200_response_inner_dict = list_workgroup_members200_response_inner_instance.to_dict()
# create an instance of ListWorkgroupMembers200ResponseInner from a dict
list_workgroup_members200_response_inner_from_dict = ListWorkgroupMembers200ResponseInner.from_dict(list_workgroup_members200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


