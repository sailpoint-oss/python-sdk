# AccountAllOfSourceOwner

The owner of this object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of owner object. | [optional] 
**id** | **str** | Identity id | [optional] 
**name** | **str** | Human-readable display name of the owner. | [optional] 

## Example

```python
from sailpoint.v3.models.account_all_of_source_owner import AccountAllOfSourceOwner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAllOfSourceOwner from a JSON string
account_all_of_source_owner_instance = AccountAllOfSourceOwner.from_json(json)
# print the JSON string representation of the object
print(AccountAllOfSourceOwner.to_json())

# convert the object into a dict
account_all_of_source_owner_dict = account_all_of_source_owner_instance.to_dict()
# create an instance of AccountAllOfSourceOwner from a dict
account_all_of_source_owner_from_dict = AccountAllOfSourceOwner.from_dict(account_all_of_source_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


