# AccountActivitySearchedItem

AccountActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**action** | **str** | Type of action performed in the activity. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**stage** | **str** | Activity&#39;s current stage. | [optional] 
**origin** | **str** | Activity&#39;s origin. | [optional] 
**status** | **str** | Activity&#39;s current status. | [optional] 
**requester** | [**AccountSource**](AccountSource.md) |  | [optional] 
**recipient** | [**AccountSource**](AccountSource.md) |  | [optional] 
**tracking_number** | **str** | Account activity&#39;s tracking number. | [optional] 
**errors** | **List[str]** | Errors provided by the source while completing account actions. | [optional] 
**warnings** | **List[str]** | Warnings provided by the source while completing account actions. | [optional] 
**approvals** | [**List[Approval1]**](Approval1.md) | Approvals performed on an item during activity. | [optional] 
**original_requests** | [**List[OriginalRequest]**](OriginalRequest.md) | Original actions that triggered all individual source actions related to the account action. | [optional] 
**expansion_items** | [**List[ExpansionItem]**](ExpansionItem.md) | Controls that translated the attribute requests into actual provisioning actions on the source. | [optional] 
**account_requests** | [**List[AccountRequest]**](AccountRequest.md) | Account data for each individual source action triggered by the original requests. | [optional] 
**sources** | **str** | Sources involved in the account activity. | [optional] 

## Example

```python
from sailpoint.v2024.models.account_activity_searched_item import AccountActivitySearchedItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivitySearchedItem from a JSON string
account_activity_searched_item_instance = AccountActivitySearchedItem.from_json(json)
# print the JSON string representation of the object
print AccountActivitySearchedItem.to_json()

# convert the object into a dict
account_activity_searched_item_dict = account_activity_searched_item_instance.to_dict()
# create an instance of AccountActivitySearchedItem from a dict
account_activity_searched_item_form_dict = account_activity_searched_item.from_dict(account_activity_searched_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


