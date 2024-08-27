# AccountAggregationCompletedStats

Overall statistics about the account aggregation.

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
from sailpoint.beta.models.account_aggregation_completed_stats import AccountAggregationCompletedStats

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAggregationCompletedStats from a JSON string
account_aggregation_completed_stats_instance = AccountAggregationCompletedStats.from_json(json)
# print the JSON string representation of the object
print(AccountAggregationCompletedStats.to_json())

# convert the object into a dict
account_aggregation_completed_stats_dict = account_aggregation_completed_stats_instance.to_dict()
# create an instance of AccountAggregationCompletedStats from a dict
account_aggregation_completed_stats_from_dict = AccountAggregationCompletedStats.from_dict(account_aggregation_completed_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


