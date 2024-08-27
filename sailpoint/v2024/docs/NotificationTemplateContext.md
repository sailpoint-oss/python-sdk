# NotificationTemplateContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, object]** | A JSON object that stores the context. | [optional] 
**created** | **datetime** | When the global context was created | [optional] 
**modified** | **datetime** | When the global context was last modified | [optional] 

## Example

```python
from sailpoint.v2024.models.notification_template_context import NotificationTemplateContext

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTemplateContext from a JSON string
notification_template_context_instance = NotificationTemplateContext.from_json(json)
# print the JSON string representation of the object
print(NotificationTemplateContext.to_json())

# convert the object into a dict
notification_template_context_dict = notification_template_context_instance.to_dict()
# create an instance of NotificationTemplateContext from a dict
notification_template_context_from_dict = NotificationTemplateContext.from_dict(notification_template_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


