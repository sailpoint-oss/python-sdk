# IdentitySyncJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job ID. | 
**status** | **str** | The job status. | 
**payload** | [**IdentitySyncPayload**](IdentitySyncPayload.md) |  | 

## Example

```python
from sailpoint.beta.models.identity_sync_job import IdentitySyncJob

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySyncJob from a JSON string
identity_sync_job_instance = IdentitySyncJob.from_json(json)
# print the JSON string representation of the object
print(IdentitySyncJob.to_json())

# convert the object into a dict
identity_sync_job_dict = identity_sync_job_instance.to_dict()
# create an instance of IdentitySyncJob from a dict
identity_sync_job_from_dict = IdentitySyncJob.from_dict(identity_sync_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


