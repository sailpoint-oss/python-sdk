# AccountUncorrelatedSource

The source the accounts are uncorrelated from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The DTO type of the source the accounts are uncorrelated from. | 
**id** | **str** | The ID of the source the accounts are uncorrelated from. | 
**name** | **str** | Display name of the source the accounts are uncorrelated from. | 

## Example

```python
from sailpoint.v2024.models.account_uncorrelated_source import AccountUncorrelatedSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUncorrelatedSource from a JSON string
account_uncorrelated_source_instance = AccountUncorrelatedSource.from_json(json)
# print the JSON string representation of the object
print(AccountUncorrelatedSource.to_json())

# convert the object into a dict
account_uncorrelated_source_dict = account_uncorrelated_source_instance.to_dict()
# create an instance of AccountUncorrelatedSource from a dict
account_uncorrelated_source_from_dict = AccountUncorrelatedSource.from_dict(account_uncorrelated_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


