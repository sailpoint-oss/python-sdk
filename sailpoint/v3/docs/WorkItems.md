# WorkItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the work item | [optional] 
**requester_id** | **str** | ID of the requester | [optional] 
**requester_display_name** | **str** | The displayname of the requester | [optional] 
**owner_id** | **str** | The ID of the owner | [optional] 
**owner_name** | **str** | The name of the owner | [optional] 
**created** | **datetime** | Time when the work item was created | [optional] 
**modified** | **datetime** | Time when the work item was last updated | [optional] 
**description** | **str** | The description of the work item | [optional] 
**state** | [**WorkItemStateManualWorkItems**](WorkItemStateManualWorkItems.md) |  | [optional] 
**type** | [**WorkItemTypeManualWorkItems**](WorkItemTypeManualWorkItems.md) |  | [optional] 
**remediation_items** | [**List[RemediationItemDetails]**](RemediationItemDetails.md) | A list of remediation items | [optional] 
**approval_items** | [**List[ApprovalItemDetails]**](ApprovalItemDetails.md) | A list of items that need to be approved | [optional] 
**name** | **str** | The work item name | [optional] 
**completed** | **datetime** | The time at which the work item completed | [optional] 
**num_items** | **int** | The number of items in the work item | [optional] 
**form** | [**WorkItemsForm**](WorkItemsForm.md) |  | [optional] 
**errors** | **List[str]** | An array of errors that ocurred during the work item | [optional] 

## Example

```python
from sailpoint.v3.models.work_items import WorkItems

# TODO update the JSON string below
json = "{}"
# create an instance of WorkItems from a JSON string
work_items_instance = WorkItems.from_json(json)
# print the JSON string representation of the object
print(WorkItems.to_json())

# convert the object into a dict
work_items_dict = work_items_instance.to_dict()
# create an instance of WorkItems from a dict
work_items_from_dict = WorkItems.from_dict(work_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


