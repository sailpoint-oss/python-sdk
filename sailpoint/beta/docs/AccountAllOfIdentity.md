# AccountAllOfIdentity

The identity this account is correlated to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the identity | [optional] 
**name** | **str** | Human-readable display name of the identity | [optional] 

## Example

```python
from sailpoint.beta.models.account_all_of_identity import AccountAllOfIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAllOfIdentity from a JSON string
account_all_of_identity_instance = AccountAllOfIdentity.from_json(json)
# print the JSON string representation of the object
print AccountAllOfIdentity.to_json()

# convert the object into a dict
account_all_of_identity_dict = account_all_of_identity_instance.to_dict()
# create an instance of AccountAllOfIdentity from a dict
account_all_of_identity_form_dict = account_all_of_identity.from_dict(account_all_of_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


