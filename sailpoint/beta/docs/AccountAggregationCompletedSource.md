# AccountAggregationCompletedSource

The source from which the accounts were aggregated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The type of object that is referenced | 
**id** | **str** | ID of the object to which this reference applies | 
**name** | **str** | Human-readable display name of the object to which this reference applies | 

## Example

```python
from beta.models.account_aggregation_completed_source import AccountAggregationCompletedSource

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


