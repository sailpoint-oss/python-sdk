# CertificationTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the certification task. | [optional] 
**type** | **str** | The type of the certification task. More values may be added in the future. | [optional] 
**target_type** | **str** | The type of item that is being operated on by this task whose ID is stored in the targetId field. | [optional] 
**target_id** | **str** | The ID of the item being operated on by this task. | [optional] 
**status** | **str** | The status of the task. | [optional] 
**errors** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) |  | [optional] 
**reassignment_trail_dtos** | [**List[ReassignmentTrailDTO]**](ReassignmentTrailDTO.md) | Reassignment trails that lead to self certification identity | [optional] 
**created** | **datetime** | The date and time on which this task was created. | [optional] 

## Example

```python
from sailpoint.v3.models.certification_task import CertificationTask

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationTask from a JSON string
certification_task_instance = CertificationTask.from_json(json)
# print the JSON string representation of the object
print(CertificationTask.to_json())

# convert the object into a dict
certification_task_dict = certification_task_instance.to_dict()
# create an instance of CertificationTask from a dict
certification_task_from_dict = CertificationTask.from_dict(certification_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


