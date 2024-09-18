# DraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique id assigned to this job. | [optional] 
**status** | **str** | Status of the job. | [optional] 
**type** | **str** | Type of the job, will always be CREATE_DRAFT for this type of job. | [optional] 
**message** | **str** | Message providing information about the outcome of the draft process. | [optional] 
**requester_name** | **str** | The name of user that that initiated the draft process. | [optional] 
**file_exists** | **bool** | Whether or not a file was generated for this draft. | [optional] [default to True]
**created** | **datetime** | The time the job was started. | [optional] 
**modified** | **datetime** | The time of the last update to the job. | [optional] 
**completed** | **datetime** | The time the job was completed. | [optional] 
**name** | **str** | Name of the draft. | [optional] 
**source_tenant** | **str** | Tenant owner of the backup from which the draft was generated. | [optional] 
**source_backup_id** | **str** | Id of the backup from which the draft was generated. | [optional] 
**source_backup_name** | **str** | Name of the backup from which the draft was generated. | [optional] 
**mode** | **str** | Denotes the origin of the source backup from which the draft was generated. - RESTORE - Same tenant. - PROMOTE - Different tenant. - UPLOAD - Uploaded configuration. | [optional] 
**approval_status** | **str** | Approval status of the draft used to determine whether or not the draft can be deployed. | [optional] 
**approval_comment** | [**List[ApprovalComment]**](ApprovalComment.md) | List of comments that have been exchanged between an approval requester and an approver. | [optional] 

## Example

```python
from sailpoint.v2024.models.draft_response import DraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DraftResponse from a JSON string
draft_response_instance = DraftResponse.from_json(json)
# print the JSON string representation of the object
print(DraftResponse.to_json())

# convert the object into a dict
draft_response_dict = draft_response_instance.to_dict()
# create an instance of DraftResponse from a dict
draft_response_from_dict = DraftResponse.from_dict(draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


