# AccountActivityDocument

AccountActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of account activity. | [optional] 
**action** | **str** | Type of action performed in the activity. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **str** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**stage** | **str** | Activity&#39;s current stage. | [optional] 
**status** | **str** | Activity&#39;s current status. | [optional] 
**requester** | [**ActivityIdentity**](ActivityIdentity.md) |  | [optional] 
**recipient** | [**ActivityIdentity**](ActivityIdentity.md) |  | [optional] 
**tracking_number** | **str** | Account activity&#39;s tracking number. | [optional] 
**errors** | **List[str]** | Errors provided by the source while completing account actions. | [optional] 
**warnings** | **List[str]** | Warnings provided by the source while completing account actions. | [optional] 
**approvals** | [**List[Approval]**](Approval.md) | Approvals performed on an item during activity. | [optional] 
**original_requests** | [**List[OriginalRequest]**](OriginalRequest.md) | Original actions that triggered all individual source actions related to the account action. | [optional] 
**expansion_items** | [**List[ExpansionItem]**](ExpansionItem.md) | Controls that translated the attribute requests into actual provisioning actions on the source. | [optional] 
**account_requests** | [**List[AccountRequest]**](AccountRequest.md) | Account data for each individual source action triggered by the original requests. | [optional] 
**sources** | **str** | Sources involved in the account activity. | [optional] 

## Example

```python
from sailpoint.v3.models.account_activity_document import AccountActivityDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivityDocument from a JSON string
account_activity_document_instance = AccountActivityDocument.from_json(json)
# print the JSON string representation of the object
print(AccountActivityDocument.to_json())

# convert the object into a dict
account_activity_document_dict = account_activity_document_instance.to_dict()
# create an instance of AccountActivityDocument from a dict
account_activity_document_from_dict = AccountActivityDocument.from_dict(account_activity_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


