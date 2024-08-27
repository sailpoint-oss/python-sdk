# SedBatchResponse

Sed Batch Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | BatchId that groups all the ids together | [optional] 

## Example

```python
from sailpoint.beta.models.sed_batch_response import SedBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SedBatchResponse from a JSON string
sed_batch_response_instance = SedBatchResponse.from_json(json)
# print the JSON string representation of the object
print(SedBatchResponse.to_json())

# convert the object into a dict
sed_batch_response_dict = sed_batch_response_instance.to_dict()
# create an instance of SedBatchResponse from a dict
sed_batch_response_from_dict = SedBatchResponse.from_dict(sed_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


