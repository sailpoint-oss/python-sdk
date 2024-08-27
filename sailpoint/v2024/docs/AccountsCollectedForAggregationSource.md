# AccountsCollectedForAggregationSource

Reference to the source that has been aggregated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the object to which this reference applies | 
**type** | **str** | The type of object that is referenced | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from sailpoint.v2024.models.accounts_collected_for_aggregation_source import AccountsCollectedForAggregationSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsCollectedForAggregationSource from a JSON string
accounts_collected_for_aggregation_source_instance = AccountsCollectedForAggregationSource.from_json(json)
# print the JSON string representation of the object
print(AccountsCollectedForAggregationSource.to_json())

# convert the object into a dict
accounts_collected_for_aggregation_source_dict = accounts_collected_for_aggregation_source_instance.to_dict()
# create an instance of AccountsCollectedForAggregationSource from a dict
accounts_collected_for_aggregation_source_from_dict = AccountsCollectedForAggregationSource.from_dict(accounts_collected_for_aggregation_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


