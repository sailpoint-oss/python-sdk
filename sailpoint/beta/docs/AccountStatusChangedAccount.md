# AccountStatusChangedAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | the ID of the account in the database | [optional] 
**native_identity** | **str** | the native identifier of the account | [optional] 
**display_name** | **str** | the display name of the account | [optional] 
**source_id** | **str** | the ID of the source for this account | [optional] 
**source_name** | **str** | the name of the source for this account | [optional] 
**entitlement_count** | **int** | the number of entitlements on this account | [optional] 
**access_type** | **str** | this value is always \&quot;account\&quot; | [optional] 

## Example

```python
from sailpoint.beta.models.account_status_changed_account import AccountStatusChangedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatusChangedAccount from a JSON string
account_status_changed_account_instance = AccountStatusChangedAccount.from_json(json)
# print the JSON string representation of the object
print(AccountStatusChangedAccount.to_json())

# convert the object into a dict
account_status_changed_account_dict = account_status_changed_account_instance.to_dict()
# create an instance of AccountStatusChangedAccount from a dict
account_status_changed_account_from_dict = AccountStatusChangedAccount.from_dict(account_status_changed_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


