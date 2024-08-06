# LoadAccountsTaskTaskMessagesInner


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
from sailpoint.v2024.models.load_accounts_task_task_messages_inner import LoadAccountsTaskTaskMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LoadAccountsTaskTaskMessagesInner from a JSON string
load_accounts_task_task_messages_inner_instance = LoadAccountsTaskTaskMessagesInner.from_json(json)
# print the JSON string representation of the object
print LoadAccountsTaskTaskMessagesInner.to_json()

# convert the object into a dict
load_accounts_task_task_messages_inner_dict = load_accounts_task_task_messages_inner_instance.to_dict()
# create an instance of LoadAccountsTaskTaskMessagesInner from a dict
load_accounts_task_task_messages_inner_form_dict = load_accounts_task_task_messages_inner.from_dict(load_accounts_task_task_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


