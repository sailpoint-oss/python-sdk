# SlimAccount


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

## Example

```python
from sailpoint.beta.models.slim_account import SlimAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SlimAccount from a JSON string
slim_account_instance = SlimAccount.from_json(json)
# print the JSON string representation of the object
print SlimAccount.to_json()

# convert the object into a dict
slim_account_dict = slim_account_instance.to_dict()
# create an instance of SlimAccount from a dict
slim_account_form_dict = slim_account.from_dict(slim_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


