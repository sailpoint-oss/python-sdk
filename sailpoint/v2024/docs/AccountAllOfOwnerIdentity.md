# AccountAllOfOwnerIdentity

The identity who owns this account, typically used for non-human accounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the identity | [optional] 
**name** | **str** | Human-readable display name of the identity | [optional] 

## Example

```python
from sailpoint.v2024.models.account_all_of_owner_identity import AccountAllOfOwnerIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAllOfOwnerIdentity from a JSON string
account_all_of_owner_identity_instance = AccountAllOfOwnerIdentity.from_json(json)
# print the JSON string representation of the object
print(AccountAllOfOwnerIdentity.to_json())

# convert the object into a dict
account_all_of_owner_identity_dict = account_all_of_owner_identity_instance.to_dict()
# create an instance of AccountAllOfOwnerIdentity from a dict
account_all_of_owner_identity_from_dict = AccountAllOfOwnerIdentity.from_dict(account_all_of_owner_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


