# AccountCorrelatedSource

The source the accounts are being correlated from.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The DTO type of the source the accounts are being correlated from. | 
**id** | **str** | The ID of the source the accounts are being correlated from. | 
**name** | **str** | Display name of the source the accounts are being correlated from. | 

## Example

```python
from sailpoint.beta.models.account_correlated_source import AccountCorrelatedSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCorrelatedSource from a JSON string
account_correlated_source_instance = AccountCorrelatedSource.from_json(json)
# print the JSON string representation of the object
print AccountCorrelatedSource.to_json()

# convert the object into a dict
account_correlated_source_dict = account_correlated_source_instance.to_dict()
# create an instance of AccountCorrelatedSource from a dict
account_correlated_source_form_dict = account_correlated_source.from_dict(account_correlated_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


