# ApprovalItems


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The approval item&#39;s ID | [optional] 
**account** | **str** | The account referenced by the approval item | [optional] 
**application** | **str** | The name of the application/source | [optional] 
**name** | **str** | The attribute&#39;s name | [optional] 
**operation** | **str** | The attribute&#39;s operation | [optional] 
**value** | **str** | The attribute&#39;s value | [optional] 
**state** | [**WorkItemState**](WorkItemState.md) |  | [optional] 

## Example

```python
from beta.models.approval_items import ApprovalItems

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalItems from a JSON string
approval_items_instance = ApprovalItems.from_json(json)
# print the JSON string representation of the object
print ApprovalItems.to_json()

# convert the object into a dict
approval_items_dict = approval_items_instance.to_dict()
# create an instance of ApprovalItems from a dict
approval_items_form_dict = approval_items.from_dict(approval_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


