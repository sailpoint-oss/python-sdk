# AggregationDocument

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
from v3.models.aggregation_document import AggregationDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationDocument from a JSON string
aggregation_document_instance = AggregationDocument.from_json(json)
# print the JSON string representation of the object
print AggregationDocument.to_json()

# convert the object into a dict
aggregation_document_dict = aggregation_document_instance.to_dict()
# create an instance of AggregationDocument from a dict
aggregation_document_form_dict = aggregation_document.from_dict(aggregation_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


