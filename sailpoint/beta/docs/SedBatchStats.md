# SedBatchStats

Sed Batch Stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_complete** | **bool** | batch complete | [optional] [default to False]
**batch_id** | **str** | batch Id | [optional] 
**discovered_count** | **int** | discovered count | [optional] 
**discovery_complete** | **bool** | discovery complete | [optional] [default to False]
**processed_count** | **int** | processed count | [optional] 

## Example

```python
from sailpoint.beta.models.sed_batch_stats import SedBatchStats

# TODO update the JSON string below
json = "{}"
# create an instance of SedBatchStats from a JSON string
sed_batch_stats_instance = SedBatchStats.from_json(json)
# print the JSON string representation of the object
print SedBatchStats.to_json()

# convert the object into a dict
sed_batch_stats_dict = sed_batch_stats_instance.to_dict()
# create an instance of SedBatchStats from a dict
sed_batch_stats_form_dict = sed_batch_stats.from_dict(sed_batch_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


