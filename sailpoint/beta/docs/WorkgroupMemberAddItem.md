# WorkgroupMemberAddItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of identity in bulk member add request. | 
**status** | **str** |  The HTTP response status code returned for an individual member that is requested for addition during a bulk add operation.   The HTTP response status code returned for an individual Governance Group is requested for deletion.   &gt; 201   - Identity is added into Governance Group members list.  &gt; 409   - Identity is already member of  Governance Group.  | 
**description** | **str** | Human readable status description and containing additional context information about success or failures etc.  | [optional] 

## Example

```python
from sailpoint.beta.models.workgroup_member_add_item import WorkgroupMemberAddItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupMemberAddItem from a JSON string
workgroup_member_add_item_instance = WorkgroupMemberAddItem.from_json(json)
# print the JSON string representation of the object
print WorkgroupMemberAddItem.to_json()

# convert the object into a dict
workgroup_member_add_item_dict = workgroup_member_add_item_instance.to_dict()
# create an instance of WorkgroupMemberAddItem from a dict
workgroup_member_add_item_form_dict = workgroup_member_add_item.from_dict(workgroup_member_add_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


