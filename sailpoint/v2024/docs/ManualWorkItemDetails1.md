# ManualWorkItemDetails1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | True if the request for this item was forwarded from one owner to another. | [optional] [default to False]
**original_owner** | [**ManualWorkItemDetailsOriginalOwner**](ManualWorkItemDetailsOriginalOwner.md) |  | [optional] 
**current_owner** | [**ManualWorkItemDetailsCurrentOwner**](ManualWorkItemDetailsCurrentOwner.md) |  | [optional] 
**modified** | **datetime** | Time at which item was modified. | [optional] 
**status** | [**ManualWorkItemState**](ManualWorkItemState.md) |  | [optional] 
**forward_history** | [**List[ApprovalForwardHistory1]**](ApprovalForwardHistory1.md) | The history of approval forward action. | [optional] 

## Example

```python
from sailpoint.v2024.models.manual_work_item_details1 import ManualWorkItemDetails1

# TODO update the JSON string below
json = "{}"
# create an instance of ManualWorkItemDetails1 from a JSON string
manual_work_item_details1_instance = ManualWorkItemDetails1.from_json(json)
# print the JSON string representation of the object
print(ManualWorkItemDetails1.to_json())

# convert the object into a dict
manual_work_item_details1_dict = manual_work_item_details1_instance.to_dict()
# create an instance of ManualWorkItemDetails1 from a dict
manual_work_item_details1_from_dict = ManualWorkItemDetails1.from_dict(manual_work_item_details1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


