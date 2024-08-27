# WorkgroupDeleteItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Governance Group. | 
**status** | **str** |  The HTTP response status code returned for an individual Governance Group that is requested for deletion during a bulk delete operation.  &gt; 204   -  Governance Group deleted successfully.  &gt; 409   - Governance Group is in use,hence can not be deleted.  &gt; 404   - Governance Group not found.  | 
**description** | **str** | Human readable status description and containing additional context information about success or failures etc.  | [optional] 

## Example

```python
from sailpoint.v2024.models.workgroup_delete_item import WorkgroupDeleteItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupDeleteItem from a JSON string
workgroup_delete_item_instance = WorkgroupDeleteItem.from_json(json)
# print the JSON string representation of the object
print(WorkgroupDeleteItem.to_json())

# convert the object into a dict
workgroup_delete_item_dict = workgroup_delete_item_instance.to_dict()
# create an instance of WorkgroupDeleteItem from a dict
workgroup_delete_item_from_dict = WorkgroupDeleteItem.from_dict(workgroup_delete_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


