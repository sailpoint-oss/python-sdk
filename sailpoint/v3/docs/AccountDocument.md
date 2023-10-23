# AccountDocument

Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**account_id** | **str** | The ID of the account | [optional] 
**source** | [**AccountSource**](AccountSource.md) |  | [optional] 
**disabled** | **bool** | Indicates if the account is disabled | [optional] 
**locked** | **bool** | Indicates if the account is locked | [optional] 
**privileged** | **bool** |  | [optional] 
**manually_correlated** | **bool** | Indicates if the account has been manually correlated to an identity | [optional] 
**password_last_set** | **datetime** | A date-time in ISO-8601 format | [optional] 
**entitlement_attributes** | **Dict[str, object]** | a map or dictionary of key/value pairs | [optional] 
**created** | **datetime** | A date-time in ISO-8601 format | [optional] 
**modified** | **datetime** | A date-time in ISO-8601 format | [optional] 
**attributes** | **Dict[str, object]** | a map or dictionary of key/value pairs | [optional] 
**identity** | [**DisplayReference**](DisplayReference.md) |  | [optional] 
**access** | [**List[AccessProfileEntitlement]**](AccessProfileEntitlement.md) |  | [optional] 
**entitlement_count** | **int** | The number of entitlements assigned to the account | [optional] 
**uncorrelated** | **bool** | Indicates if the account is not correlated to an identity | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from v3.models.account_document import AccountDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDocument from a JSON string
account_document_instance = AccountDocument.from_json(json)
# print the JSON string representation of the object
print AccountDocument.to_json()

# convert the object into a dict
account_document_dict = account_document_instance.to_dict()
# create an instance of AccountDocument from a dict
account_document_form_dict = account_document.from_dict(account_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


