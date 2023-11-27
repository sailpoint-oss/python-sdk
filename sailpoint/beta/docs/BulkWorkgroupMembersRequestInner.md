# BulkWorkgroupMembersRequestInner

Identity's basic details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identity&#39;s DTO type. | [optional] 
**id** | **str** | Identity ID. | [optional] 
**name** | **str** | Identity&#39;s display name. | [optional] 

## Example

```python
from sailpoint.beta.models.bulk_workgroup_members_request_inner import BulkWorkgroupMembersRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWorkgroupMembersRequestInner from a JSON string
bulk_workgroup_members_request_inner_instance = BulkWorkgroupMembersRequestInner.from_json(json)
# print the JSON string representation of the object
print BulkWorkgroupMembersRequestInner.to_json()

# convert the object into a dict
bulk_workgroup_members_request_inner_dict = bulk_workgroup_members_request_inner_instance.to_dict()
# create an instance of BulkWorkgroupMembersRequestInner from a dict
bulk_workgroup_members_request_inner_form_dict = bulk_workgroup_members_request_inner.from_dict(bulk_workgroup_members_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


