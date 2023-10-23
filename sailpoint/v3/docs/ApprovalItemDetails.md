# ApprovalItemDetails


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
from v3.models.approval_item_details import ApprovalItemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalItemDetails from a JSON string
approval_item_details_instance = ApprovalItemDetails.from_json(json)
# print the JSON string representation of the object
print ApprovalItemDetails.to_json()

# convert the object into a dict
approval_item_details_dict = approval_item_details_instance.to_dict()
# create an instance of ApprovalItemDetails from a dict
approval_item_details_form_dict = approval_item_details.from_dict(approval_item_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


