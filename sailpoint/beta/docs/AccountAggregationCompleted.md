# AccountAggregationCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**AccountAggregationCompletedSource**](AccountAggregationCompletedSource.md) |  | 
**status** | **object** | The overall status of the aggregation. | 
**started** | **datetime** | The date and time when the account aggregation started. | 
**completed** | **datetime** | The date and time when the account aggregation finished. | 
**errors** | **List[str]** | A list of errors that occurred during the aggregation. | 
**warnings** | **List[str]** | A list of warnings that occurred during the aggregation. | 
**stats** | [**AccountAggregationCompletedStats**](AccountAggregationCompletedStats.md) |  | 

## Example

```python
from sailpoint.beta.models.account_aggregation_completed import AccountAggregationCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAggregationCompleted from a JSON string
account_aggregation_completed_instance = AccountAggregationCompleted.from_json(json)
# print the JSON string representation of the object
print AccountAggregationCompleted.to_json()

# convert the object into a dict
account_aggregation_completed_dict = account_aggregation_completed_instance.to_dict()
# create an instance of AccountAggregationCompleted from a dict
account_aggregation_completed_form_dict = account_aggregation_completed.from_dict(account_aggregation_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


