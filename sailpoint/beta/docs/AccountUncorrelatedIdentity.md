# AccountUncorrelatedIdentity

Identity the account is uncorrelated with.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of the identity the account is uncorrelated with. | 
**id** | **str** | ID of the identity the account is uncorrelated with. | 
**name** | **str** | Display name of the identity the account is uncorrelated with. | 

## Example

```python
from sailpoint.beta.models.account_uncorrelated_identity import AccountUncorrelatedIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUncorrelatedIdentity from a JSON string
account_uncorrelated_identity_instance = AccountUncorrelatedIdentity.from_json(json)
# print the JSON string representation of the object
print AccountUncorrelatedIdentity.to_json()

# convert the object into a dict
account_uncorrelated_identity_dict = account_uncorrelated_identity_instance.to_dict()
# create an instance of AccountUncorrelatedIdentity from a dict
account_uncorrelated_identity_form_dict = account_uncorrelated_identity.from_dict(account_uncorrelated_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


