# SedBatchStatus

Sed Batch Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status of batch | [optional] 

## Example

```python
from sailpoint.v2024.models.sed_batch_status import SedBatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SedBatchStatus from a JSON string
sed_batch_status_instance = SedBatchStatus.from_json(json)
# print the JSON string representation of the object
print SedBatchStatus.to_json()

# convert the object into a dict
sed_batch_status_dict = sed_batch_status_instance.to_dict()
# create an instance of SedBatchStatus from a dict
sed_batch_status_form_dict = sed_batch_status.from_dict(sed_batch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


