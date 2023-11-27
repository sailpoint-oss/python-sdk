# ProcessingDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | A date-time in ISO-8601 format | [optional] 
**stage** | **str** |  | [optional] 
**retry_count** | **int** |  | [optional] 
**stack_trace** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sailpoint.v3.models.processing_details import ProcessingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingDetails from a JSON string
processing_details_instance = ProcessingDetails.from_json(json)
# print the JSON string representation of the object
print ProcessingDetails.to_json()

# convert the object into a dict
processing_details_dict = processing_details_instance.to_dict()
# create an instance of ProcessingDetails from a dict
processing_details_form_dict = processing_details.from_dict(processing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


