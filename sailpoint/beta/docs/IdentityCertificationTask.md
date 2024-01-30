# IdentityCertificationTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The task id | [optional] 
**certification_id** | **str** | The certification id | [optional] 
**type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**errors** | **List[str]** | Any errors executing the task (Optional). | [optional] 

## Example

```python
from sailpoint.beta.models.identity_certification_task import IdentityCertificationTask

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCertificationTask from a JSON string
identity_certification_task_instance = IdentityCertificationTask.from_json(json)
# print the JSON string representation of the object
print IdentityCertificationTask.to_json()

# convert the object into a dict
identity_certification_task_dict = identity_certification_task_instance.to_dict()
# create an instance of IdentityCertificationTask from a dict
identity_certification_task_form_dict = identity_certification_task.from_dict(identity_certification_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


