# TaskResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | the type of response reference | [optional] 
**id** | **str** | the task ID | [optional] 
**name** | **str** | the task name (not used in this endpoint, always null) | [optional] 

## Example

```python
from sailpoint.v2024.models.task_result_response import TaskResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultResponse from a JSON string
task_result_response_instance = TaskResultResponse.from_json(json)
# print the JSON string representation of the object
print TaskResultResponse.to_json()

# convert the object into a dict
task_result_response_dict = task_result_response_instance.to_dict()
# create an instance of TaskResultResponse from a dict
task_result_response_form_dict = task_result_response.from_dict(task_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


