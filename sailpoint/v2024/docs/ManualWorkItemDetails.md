# ManualWorkItemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarded** | **bool** | True if the request for this item was forwarded from one owner to another. | [optional] [default to False]
**original_owner** | [**ManualWorkItemDetailsOriginalOwner**](ManualWorkItemDetailsOriginalOwner.md) |  | [optional] 
**current_owner** | [**ManualWorkItemDetailsCurrentOwner**](ManualWorkItemDetailsCurrentOwner.md) |  | [optional] 
**modified** | **datetime** | Time at which item was modified. | [optional] 
**status** | [**ManualWorkItemState**](ManualWorkItemState.md) |  | [optional] 
**forward_history** | [**List[ApprovalForwardHistory]**](ApprovalForwardHistory.md) | The history of approval forward action. | [optional] 

## Example

```python
from sailpoint.v2024.models.manual_work_item_details import ManualWorkItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ManualWorkItemDetails from a JSON string
manual_work_item_details_instance = ManualWorkItemDetails.from_json(json)
# print the JSON string representation of the object
print(ManualWorkItemDetails.to_json())

# convert the object into a dict
manual_work_item_details_dict = manual_work_item_details_instance.to_dict()
# create an instance of ManualWorkItemDetails from a dict
manual_work_item_details_from_dict = ManualWorkItemDetails.from_dict(manual_work_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


