# WorkItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the work item | [optional] 
**requester_id** | **str** | ID of the requester | [optional] 
**requester_display_name** | **str** | The displayname of the requester | [optional] 
**owner_id** | **str** | The ID of the owner | [optional] 
**owner_name** | **str** | The name of the owner | [optional] 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**description** | **str** | The description of the work item | [optional] 
**state** | [**WorkItemState**](WorkItemState.md) |  | [optional] 
**type** | [**WorkItemType**](WorkItemType.md) |  | [optional] 
**remediation_items** | [**RemediationItemDetails**](RemediationItemDetails.md) |  | [optional] 
**approval_items** | [**ApprovalItemDetails**](ApprovalItemDetails.md) |  | [optional] 
**name** | **str** | The work item name | [optional] 
**completed** | **datetime** |  | [optional] 
**num_items** | **int** | The number of items in the work item | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from sailpoint.beta.models.work_items import WorkItems

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItems from a JSON string
work_items_instance = WorkItems.from_json(json)
# print the JSON string representation of the object
print WorkItems.to_json()

# convert the object into a dict
work_items_dict = work_items_instance.to_dict()
# create an instance of WorkItems from a dict
work_items_form_dict = work_items.from_dict(work_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


