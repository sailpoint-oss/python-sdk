# NonEmployeeBulkUploadStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Returns the following values indicating the progress or result of the bulk upload job. \&quot;PENDING\&quot; means the job is queued and waiting to be processed. \&quot;IN_PROGRESS\&quot; means the job is currently being processed. \&quot;COMPLETED\&quot; means the job has been completed without any errors. \&quot;ERROR\&quot; means the job failed to process with errors. null means job has been submitted to the source.  | [optional] 

## Example

```python
from sailpoint.v2024.models.non_employee_bulk_upload_status import NonEmployeeBulkUploadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NonEmployeeBulkUploadStatus from a JSON string
non_employee_bulk_upload_status_instance = NonEmployeeBulkUploadStatus.from_json(json)
# print the JSON string representation of the object
print NonEmployeeBulkUploadStatus.to_json()

# convert the object into a dict
non_employee_bulk_upload_status_dict = non_employee_bulk_upload_status_instance.to_dict()
# create an instance of NonEmployeeBulkUploadStatus from a dict
non_employee_bulk_upload_status_form_dict = non_employee_bulk_upload_status.from_dict(non_employee_bulk_upload_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


