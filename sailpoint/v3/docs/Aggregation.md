# Aggregation

Aggregation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | [**DocumentType**](DocumentType.md) |  | 
**status** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**avg_duration** | **int** |  | [optional] 
**changed_accounts** | **int** |  | [optional] 
**next_scheduled** | **datetime** | A date-time in ISO-8601 format | [optional] 
**start_time** | **datetime** | A date-time in ISO-8601 format | [optional] 
**source_owner** | **str** | John Doe | [optional] 

## Example

```python
from v3.models.aggregation import Aggregation

# TODO update the JSON string below
json = "{}"
# create an instance of Aggregation from a JSON string
aggregation_instance = Aggregation.from_json(json)
# print the JSON string representation of the object
print Aggregation.to_json()

# convert the object into a dict
aggregation_dict = aggregation_instance.to_dict()
# create an instance of Aggregation from a dict
aggregation_form_dict = aggregation.from_dict(aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


