# AccountAttributesChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**AccountAttributesChangedIdentity**](AccountAttributesChangedIdentity.md) |  | 
**source** | [**AccountAttributesChangedSource**](AccountAttributesChangedSource.md) |  | 
**account** | [**AccountAttributesChangedAccount**](AccountAttributesChangedAccount.md) |  | 
**changes** | [**List[AccountAttributesChangedChangesInner]**](AccountAttributesChangedChangesInner.md) | A list of attributes that changed. | 

## Example

```python
from sailpoint.v2024.models.account_attributes_changed import AccountAttributesChanged

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAttributesChanged from a JSON string
account_attributes_changed_instance = AccountAttributesChanged.from_json(json)
# print the JSON string representation of the object
print(AccountAttributesChanged.to_json())

# convert the object into a dict
account_attributes_changed_dict = account_attributes_changed_instance.to_dict()
# create an instance of AccountAttributesChanged from a dict
account_attributes_changed_from_dict = AccountAttributesChanged.from_dict(account_attributes_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


