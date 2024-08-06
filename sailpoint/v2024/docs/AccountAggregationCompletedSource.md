# AccountAggregationCompletedSource

The source the accounts are being aggregated from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The DTO type of the source the accounts are being aggregated from. | 
**id** | **str** | The ID of the source the accounts are being aggregated from. | 
**name** | **str** | Display name of the source the accounts are being aggregated from. | 

## Example

```python
from sailpoint.v2024.models.account_aggregation_completed_source import AccountAggregationCompletedSource

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAggregationCompletedSource from a JSON string
account_aggregation_completed_source_instance = AccountAggregationCompletedSource.from_json(json)
# print the JSON string representation of the object
print AccountAggregationCompletedSource.to_json()

# convert the object into a dict
account_aggregation_completed_source_dict = account_aggregation_completed_source_instance.to_dict()
# create an instance of AccountAggregationCompletedSource from a dict
account_aggregation_completed_source_form_dict = account_aggregation_completed_source.from_dict(account_aggregation_completed_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


