# AccountUncorrelatedIdentity

The identity that the account uncorrelated with.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.account_uncorrelated_identity import AccountUncorrelatedIdentity

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


