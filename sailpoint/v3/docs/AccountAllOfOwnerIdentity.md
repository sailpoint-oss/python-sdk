# AccountAllOfOwnerIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 

## Example

```python
from sailpoint.v3.models.account_all_of_owner_identity import AccountAllOfOwnerIdentity

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


