# FullAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | System-generated unique ID of the Object | [optional] [readonly] 
**name** | **str** | Name of the Object | 
**created** | **datetime** | Creation date of the Object | [optional] [readonly] 
**modified** | **datetime** | Last modification date of the Object | [optional] [readonly] 
**uuid** | **str** | Unique ID from the owning source | [optional] 
**native_identity** | **str** | The native identifier of the account | [optional] 
**description** | **str** | The description for the account | [optional] 
**disabled** | **bool** | Whether the account is disabled | [optional] 
**locked** | **bool** | Whether the account is locked | [optional] 
**manually_correlated** | **bool** | Whether the account was manually correlated | [optional] 
**has_entitlements** | **bool** | Whether the account has any entitlements associated with it | [optional] 
**source_id** | **str** | The ID of the source for which this account belongs | [optional] 
**source_name** | **str** | The name of the source | [optional] 
**identity_id** | **str** | The ID of the identity for which this account is correlated to if not uncorrelated | [optional] 
**attributes** | **Dict[str, object]** | A map containing attributes associated with the account | [optional] 
**authoritative** | **bool** | Whether this account belongs to an authoritative source | [optional] 
**system_account** | **bool** | Whether this account is for the IdentityNow source | [optional] 
**uncorrelated** | **bool** | True if this account is not correlated to an identity | [optional] 
**features** | **str** | A string list containing the owning source&#39;s features | [optional] 

## Example

```python
from beta.models.full_account import FullAccount

# TODO update the JSON string below
json = "{}"
# create an instance of FullAccount from a JSON string
full_account_instance = FullAccount.from_json(json)
# print the JSON string representation of the object
print FullAccount.to_json()

# convert the object into a dict
full_account_dict = full_account_instance.to_dict()
# create an instance of FullAccount from a dict
full_account_form_dict = full_account.from_dict(full_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


