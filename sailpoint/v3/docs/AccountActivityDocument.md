# AccountActivityDocument

AccountActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**action** | **str** | The type of action that this activity performed | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**stage** | **str** | The current stage of the activity | [optional] 
**origin** | **str** |  | [optional] 
**status** | **str** | the current status of the activity | [optional] 
**requester** | [**AccountSource**](AccountSource.md) |  | [optional] 
**recipient** | [**AccountSource**](AccountSource.md) |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**approvals** | [**List[Approval]**](Approval.md) |  | [optional] 
**original_requests** | [**List[OriginalRequest]**](OriginalRequest.md) |  | [optional] 
**expansion_items** | [**List[ExpansionItem]**](ExpansionItem.md) |  | [optional] 
**account_requests** | [**List[AccountRequest]**](AccountRequest.md) |  | [optional] 
**sources** | **str** |  | [optional] 

## Example

```python
from v3.models.account_activity_document import AccountActivityDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivityDocument from a JSON string
account_activity_document_instance = AccountActivityDocument.from_json(json)
# print the JSON string representation of the object
print AccountActivityDocument.to_json()

# convert the object into a dict
account_activity_document_dict = account_activity_document_instance.to_dict()
# create an instance of AccountActivityDocument from a dict
account_activity_document_form_dict = account_activity_document.from_dict(account_activity_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


