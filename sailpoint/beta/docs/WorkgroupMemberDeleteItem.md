# WorkgroupMemberDeleteItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of identity in bulk member add /remove request. | 
**status** | **str** |  The HTTP response status code returned for an individual  member that is requested for deletion during a bulk delete operation.  &gt; 204   - Identity is removed from Governance Group members list.  &gt; 404   - Identity is not member of Governance Group.  | 
**description** | **str** | Human readable status description and containing additional context information about success or failures etc.  | [optional] 

## Example

```python
from sailpoint.beta.models.workgroup_member_delete_item import WorkgroupMemberDeleteItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupMemberDeleteItem from a JSON string
workgroup_member_delete_item_instance = WorkgroupMemberDeleteItem.from_json(json)
# print the JSON string representation of the object
print WorkgroupMemberDeleteItem.to_json()

# convert the object into a dict
workgroup_member_delete_item_dict = workgroup_member_delete_item_instance.to_dict()
# create an instance of WorkgroupMemberDeleteItem from a dict
workgroup_member_delete_item_form_dict = workgroup_member_delete_item.from_dict(workgroup_member_delete_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


