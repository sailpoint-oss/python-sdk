# UploadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique id assigned to this job. | 
**status** | **str** | Status of the job. | 
**type** | **str** | Type of the job, either Backup or Draft. | 
**tenant** | **str** | The name of the tenant performing the upload | [optional] 
**requester_name** | **str** | The name of the requester. | [optional] 
**created** | **datetime** | The time the job was started. | 
**modified** | **datetime** | The time of the last update to the job. | 
**name** | **str** | The name assigned to the upload file in the request body. | [optional] 
**user_can_delete** | **bool** | Is the job a regular backup job, if so is the user allowed to delete the backup file. Since this is an upload job it remains as false. | [optional] [default to True]
**is_partial** | **bool** | Is the job a regular backup job, if so is it partial. Since this is an upload job it remains as false. | [optional] [default to False]
**backup_type** | **str** | What kind of backup is this being treated as. | [optional] 
**hydration_status** | **str** | have the objects contained in the upload file been hydrated. | [optional] 

## Example

```python
from sailpoint.v3.models.uploads_request import UploadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadsRequest from a JSON string
uploads_request_instance = UploadsRequest.from_json(json)
# print the JSON string representation of the object
print UploadsRequest.to_json()

# convert the object into a dict
uploads_request_dict = uploads_request_instance.to_dict()
# create an instance of UploadsRequest from a dict
uploads_request_form_dict = uploads_request.from_dict(uploads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


