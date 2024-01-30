# TaskStatusMessage

TaskStatus Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message | 
**localized_text** | [**LocalizedMessage**](LocalizedMessage.md) |  | 
**key** | **str** | Key of the message | 
**parameters** | **List[object]** | Message parameters for internationalization | 

## Example

```python
from sailpoint.beta.models.task_status_message import TaskStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatusMessage from a JSON string
task_status_message_instance = TaskStatusMessage.from_json(json)
# print the JSON string representation of the object
print TaskStatusMessage.to_json()

# convert the object into a dict
task_status_message_dict = task_status_message_instance.to_dict()
# create an instance of TaskStatusMessage from a dict
task_status_message_form_dict = task_status_message.from_dict(task_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


