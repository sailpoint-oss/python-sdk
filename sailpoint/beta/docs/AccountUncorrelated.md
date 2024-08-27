# AccountUncorrelated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**AccountUncorrelatedIdentity**](AccountUncorrelatedIdentity.md) |  | 
**source** | [**AccountUncorrelatedSource**](AccountUncorrelatedSource.md) |  | 
**account** | [**AccountUncorrelatedAccount**](AccountUncorrelatedAccount.md) |  | 
**entitlement_count** | **int** | The number of entitlements associated with this account. | [optional] 

## Example

```python
from sailpoint.beta.models.account_uncorrelated import AccountUncorrelated

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUncorrelated from a JSON string
account_uncorrelated_instance = AccountUncorrelated.from_json(json)
# print the JSON string representation of the object
print(AccountUncorrelated.to_json())

# convert the object into a dict
account_uncorrelated_dict = account_uncorrelated_instance.to_dict()
# create an instance of AccountUncorrelated from a dict
account_uncorrelated_from_dict = AccountUncorrelated.from_dict(account_uncorrelated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


