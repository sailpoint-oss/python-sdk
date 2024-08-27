# TaskResultDto

Task result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Task result DTO type. | [optional] 
**id** | **str** | Task result ID. | [optional] 
**name** | **str** | Task result display name. | [optional] 

## Example

```python
from sailpoint.v2024.models.task_result_dto import TaskResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultDto from a JSON string
task_result_dto_instance = TaskResultDto.from_json(json)
# print the JSON string representation of the object
print(TaskResultDto.to_json())

# convert the object into a dict
task_result_dto_dict = task_result_dto_instance.to_dict()
# create an instance of TaskResultDto from a dict
task_result_dto_from_dict = TaskResultDto.from_dict(task_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


