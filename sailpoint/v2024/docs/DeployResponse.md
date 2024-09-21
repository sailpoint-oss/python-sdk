# DeployResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique id assigned to this job. | [optional] 
**status** | **str** | Status of the job. | [optional] 
**type** | **str** | Type of the job, will always be CONFIG_DEPLOY_DRAFT for this type of job. | [optional] 
**message** | **str** | Message providing information about the outcome of the deploy process. | [optional] 
**requester_name** | **str** | The name of the user that initiated the deploy process. | [optional] 
**file_exists** | **bool** | Whether or not a results file was created and stored for this deploy. | [optional] [default to True]
**created** | **datetime** | The time the job was started. | [optional] 
**modified** | **datetime** | The time of the last update to the job. | [optional] 
**completed** | **datetime** | The time the job was completed. | [optional] 
**draft_id** | **str** | The id of the draft that was used for this deploy. | [optional] 
**draft_name** | **str** | The name of the draft that was used for this deploy. | [optional] 
**cloud_storage_status** | **str** | Whether this deploy results file has been transferred to a customer storage location. | [optional] 

## Example

```python
from sailpoint.v2024.models.deploy_response import DeployResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeployResponse from a JSON string
deploy_response_instance = DeployResponse.from_json(json)
# print the JSON string representation of the object
print(DeployResponse.to_json())

# convert the object into a dict
deploy_response_dict = deploy_response_instance.to_dict()
# create an instance of DeployResponse from a dict
deploy_response_from_dict = DeployResponse.from_dict(deploy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


