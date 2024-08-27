# AccountsCollectedForAggregationStats

Overall statistics about the account collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scanned** | **int** | The number of accounts which were scanned / iterated over. | 
**unchanged** | **int** | The number of accounts which existed before, but had no changes. | 
**changed** | **int** | The number of accounts which existed before, but had changes. | 
**added** | **int** | The number of accounts which are new - have not existed before. | 
**removed** | **int** | The number accounts which existed before, but no longer exist (thus getting removed). | 

## Example

```python
from sailpoint.v2024.models.accounts_collected_for_aggregation_stats import AccountsCollectedForAggregationStats

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsCollectedForAggregationStats from a JSON string
accounts_collected_for_aggregation_stats_instance = AccountsCollectedForAggregationStats.from_json(json)
# print the JSON string representation of the object
print(AccountsCollectedForAggregationStats.to_json())

# convert the object into a dict
accounts_collected_for_aggregation_stats_dict = accounts_collected_for_aggregation_stats_instance.to_dict()
# create an instance of AccountsCollectedForAggregationStats from a dict
accounts_collected_for_aggregation_stats_from_dict = AccountsCollectedForAggregationStats.from_dict(accounts_collected_for_aggregation_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


