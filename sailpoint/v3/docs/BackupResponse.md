# BackupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique id assigned to this backup. | [optional] 
**status** | **str** | Status of the backup. | [optional] 
**type** | **str** | Type of the job, will always be BACKUP for this type of job. | [optional] 
**tenant** | **str** | The name of the tenant performing the upload | [optional] 
**requester_name** | **str** | The name of the requester. | [optional] 
**file_exists** | **bool** | Whether or not a file was created and stored for this backup. | [optional] [default to True]
**created** | **datetime** | The time the job was started. | [optional] 
**modified** | **datetime** | The time of the last update to the job. | [optional] 
**completed** | **datetime** | The time the job was completed. | [optional] 
**name** | **str** | The name assigned to the upload file in the request body. | [optional] 
**user_can_delete** | **bool** | Whether this backup can be deleted by a regular user. | [optional] [default to True]
**is_partial** | **bool** | Whether this backup contains all supported object types or only some of them. | [optional] [default to False]
**backup_type** | **str** | Denotes how this backup was created. - MANUAL - The backup was created by a user. - AUTOMATED - The backup was created by devops. - AUTOMATED_DRAFT - The backup was created during a draft process. - UPLOADED - The backup was created by uploading an existing configuration file. | [optional] 
**options** | [**BackupOptions**](BackupOptions.md) |  | [optional] 
**hydration_status** | **str** | Whether the object details of this backup are ready. | [optional] 
**total_object_count** | **int** | Number of objects contained in this backup. | [optional] 
**cloud_storage_status** | **str** | Whether this backup has been transferred to a customer storage location. | [optional] 

## Example

```python
from sailpoint.v3.models.backup_response import BackupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BackupResponse from a JSON string
backup_response_instance = BackupResponse.from_json(json)
# print the JSON string representation of the object
print(BackupResponse.to_json())

# convert the object into a dict
backup_response_dict = backup_response_instance.to_dict()
# create an instance of BackupResponse from a dict
backup_response_from_dict = BackupResponse.from_dict(backup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


