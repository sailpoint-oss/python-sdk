# AccountUncorrelatedAccount

Uncorrelated account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Uncorrelated account&#39;s DTO type. | 
**id** | **str** | Uncorrelated account&#39;s ID. | 
**name** | **str** | Uncorrelated account&#39;s display name. | 
**native_identity** | **str** | Unique ID of the account on the source. | 
**uuid** | **str** | The source&#39;s unique identifier for the account. UUID is generated by the source system. | [optional] 

## Example

```python
from sailpoint.beta.models.account_uncorrelated_account import AccountUncorrelatedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUncorrelatedAccount from a JSON string
account_uncorrelated_account_instance = AccountUncorrelatedAccount.from_json(json)
# print the JSON string representation of the object
print(AccountUncorrelatedAccount.to_json())

# convert the object into a dict
account_uncorrelated_account_dict = account_uncorrelated_account_instance.to_dict()
# create an instance of AccountUncorrelatedAccount from a dict
account_uncorrelated_account_from_dict = AccountUncorrelatedAccount.from_dict(account_uncorrelated_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


