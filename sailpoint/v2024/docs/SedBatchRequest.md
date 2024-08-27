# SedBatchRequest

Sed Batch Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | **List[str]** | list of entitlement ids | [optional] 

## Example

```python
from sailpoint.v2024.models.sed_batch_request import SedBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SedBatchRequest from a JSON string
sed_batch_request_instance = SedBatchRequest.from_json(json)
# print the JSON string representation of the object
print(SedBatchRequest.to_json())

# convert the object into a dict
sed_batch_request_dict = sed_batch_request_instance.to_dict()
# create an instance of SedBatchRequest from a dict
sed_batch_request_from_dict = SedBatchRequest.from_dict(sed_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


