# TaskResultDetailsMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the message. | [optional] 
**error** | **bool** | Flag whether message is an error. | [optional] [default to False]
**warning** | **bool** | Flag whether message is a warning. | [optional] [default to False]
**key** | **str** | Message string identifier. | [optional] 
**localized_text** | **str** | Message context with the locale based language. | [optional] 

## Example

```python
from sailpoint.v3.models.task_result_details_messages_inner import TaskResultDetailsMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResultDetailsMessagesInner from a JSON string
task_result_details_messages_inner_instance = TaskResultDetailsMessagesInner.from_json(json)
# print the JSON string representation of the object
print TaskResultDetailsMessagesInner.to_json()

# convert the object into a dict
task_result_details_messages_inner_dict = task_result_details_messages_inner_instance.to_dict()
# create an instance of TaskResultDetailsMessagesInner from a dict
task_result_details_messages_inner_form_dict = task_result_details_messages_inner.from_dict(task_result_details_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


