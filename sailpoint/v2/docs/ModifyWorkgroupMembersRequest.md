# ModifyWorkgroupMembersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** |  | [optional] 
**remove** | **List[str]** |  | [optional] 

## Example

```python
from v2.models.modify_workgroup_members_request import ModifyWorkgroupMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyWorkgroupMembersRequest from a JSON string
modify_workgroup_members_request_instance = ModifyWorkgroupMembersRequest.from_json(json)
# print the JSON string representation of the object
print ModifyWorkgroupMembersRequest.to_json()

# convert the object into a dict
modify_workgroup_members_request_dict = modify_workgroup_members_request_instance.to_dict()
# create an instance of ModifyWorkgroupMembersRequest from a dict
modify_workgroup_members_request_form_dict = modify_workgroup_members_request.from_dict(modify_workgroup_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


