# AccountsCollectedForAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**AccountsCollectedForAggregationSource**](AccountsCollectedForAggregationSource.md) |  | 
**status** | **object** | The overall status of the collection. | 
**started** | **datetime** | The date and time when the account collection started. | 
**completed** | **datetime** | The date and time when the account collection finished. | 
**errors** | **List[str]** | A list of errors that occurred during the collection. | 
**warnings** | **List[str]** | A list of warnings that occurred during the collection. | 
**stats** | [**AccountsCollectedForAggregationStats**](AccountsCollectedForAggregationStats.md) |  | 

## Example

```python
from sailpoint.v2024.models.accounts_collected_for_aggregation import AccountsCollectedForAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsCollectedForAggregation from a JSON string
accounts_collected_for_aggregation_instance = AccountsCollectedForAggregation.from_json(json)
# print the JSON string representation of the object
print(AccountsCollectedForAggregation.to_json())

# convert the object into a dict
accounts_collected_for_aggregation_dict = accounts_collected_for_aggregation_instance.to_dict()
# create an instance of AccountsCollectedForAggregation from a dict
accounts_collected_for_aggregation_from_dict = AccountsCollectedForAggregation.from_dict(accounts_collected_for_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


