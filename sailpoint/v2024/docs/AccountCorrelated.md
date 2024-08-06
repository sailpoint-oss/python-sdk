# AccountCorrelated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**AccountCorrelatedIdentity**](AccountCorrelatedIdentity.md) |  | 
**source** | [**AccountCorrelatedSource**](AccountCorrelatedSource.md) |  | 
**account** | [**AccountCorrelatedAccount**](AccountCorrelatedAccount.md) |  | 
**attributes** | **Dict[str, object]** | The attributes associated with the account.  Attributes are unique per source. | 
**entitlement_count** | **int** | The number of entitlements associated with this account. | [optional] 

## Example

```python
from sailpoint.v2024.models.account_correlated import AccountCorrelated

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCorrelated from a JSON string
account_correlated_instance = AccountCorrelated.from_json(json)
# print the JSON string representation of the object
print AccountCorrelated.to_json()

# convert the object into a dict
account_correlated_dict = account_correlated_instance.to_dict()
# create an instance of AccountCorrelated from a dict
account_correlated_form_dict = account_correlated.from_dict(account_correlated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


