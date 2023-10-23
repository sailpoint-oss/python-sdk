# SourceSyncJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job ID. | 
**status** | **str** | The job status. | 
**payload** | [**SourceSyncPayload**](SourceSyncPayload.md) |  | 

## Example

```python
from beta.models.source_sync_job import SourceSyncJob

# TODO update the JSON string below
json = "{}"
# create an instance of SourceSyncJob from a JSON string
source_sync_job_instance = SourceSyncJob.from_json(json)
# print the JSON string representation of the object
print SourceSyncJob.to_json()

# convert the object into a dict
source_sync_job_dict = source_sync_job_instance.to_dict()
# create an instance of SourceSyncJob from a dict
source_sync_job_form_dict = source_sync_job.from_dict(source_sync_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


