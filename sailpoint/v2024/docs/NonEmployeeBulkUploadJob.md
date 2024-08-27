# NonEmployeeBulkUploadJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The bulk upload job&#39;s ID. (UUID) | [optional] 
**source_id** | **str** | The ID of the source to bulk-upload non-employees to. (UUID) | [optional] 
**created** | **datetime** | The date-time the job was submitted. | [optional] 
**modified** | **datetime** | The date-time that the job was last updated. | [optional] 
**status** | **str** | Returns the following values indicating the progress or result of the bulk upload job. \&quot;PENDING\&quot; means the job is queued and waiting to be processed. \&quot;IN_PROGRESS\&quot; means the job is currently being processed. \&quot;COMPLETED\&quot; means the job has been completed without any errors. \&quot;ERROR\&quot; means the job failed to process with errors.  | [optional] 

## Example

```python
from sailpoint.v2024.models.non_employee_bulk_upload_job import NonEmployeeBulkUploadJob

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeBulkUploadJob from a JSON string
non_employee_bulk_upload_job_instance = NonEmployeeBulkUploadJob.from_json(json)
# print the JSON string representation of the object
print(NonEmployeeBulkUploadJob.to_json())

# convert the object into a dict
non_employee_bulk_upload_job_dict = non_employee_bulk_upload_job_instance.to_dict()
# create an instance of NonEmployeeBulkUploadJob from a dict
non_employee_bulk_upload_job_from_dict = NonEmployeeBulkUploadJob.from_dict(non_employee_bulk_upload_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


