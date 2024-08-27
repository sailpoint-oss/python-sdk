# SpConfigImportJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique id assigned to this job. | 
**status** | **str** | Status of the job. | 
**type** | **str** | Type of the job, either export or import. | 
**expiration** | **datetime** | The time until which the artifacts will be available for download. | 
**created** | **datetime** | The time the job was started. | 
**modified** | **datetime** | The time of the last update to the job. | 
**message** | **str** | This message contains additional information about the overall status of the job. | 
**completed** | **datetime** | The time the job was completed. | 

## Example

```python
from sailpoint.v2024.models.sp_config_import_job_status import SpConfigImportJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SpConfigImportJobStatus from a JSON string
sp_config_import_job_status_instance = SpConfigImportJobStatus.from_json(json)
# print the JSON string representation of the object
print(SpConfigImportJobStatus.to_json())

# convert the object into a dict
sp_config_import_job_status_dict = sp_config_import_job_status_instance.to_dict()
# create an instance of SpConfigImportJobStatus from a dict
sp_config_import_job_status_from_dict = SpConfigImportJobStatus.from_dict(sp_config_import_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


