# AccountAllOfOwnerGroup

The governance group who owns this account, typically used for non-human accounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object being referenced | [optional] 
**id** | **str** | ID of the governance group | [optional] 
**name** | **str** | Human-readable display name of the governance group | [optional] 

## Example

```python
from sailpoint.beta.models.account_all_of_owner_group import AccountAllOfOwnerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAllOfOwnerGroup from a JSON string
account_all_of_owner_group_instance = AccountAllOfOwnerGroup.from_json(json)
# print the JSON string representation of the object
print(AccountAllOfOwnerGroup.to_json())

# convert the object into a dict
account_all_of_owner_group_dict = account_all_of_owner_group_instance.to_dict()
# create an instance of AccountAllOfOwnerGroup from a dict
account_all_of_owner_group_from_dict = AccountAllOfOwnerGroup.from_dict(account_all_of_owner_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


