# SendTestNotificationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The template notification key. | [optional] 
**medium** | **str** | The notification medium. Has to be one of the following enum values. | [optional] 
**context** | **object** | A Json object that denotes the context specific to the template. | [optional] 

## Example

```python
from sailpoint.beta.models.send_test_notification_request_dto import SendTestNotificationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SendTestNotificationRequestDto from a JSON string
send_test_notification_request_dto_instance = SendTestNotificationRequestDto.from_json(json)
# print the JSON string representation of the object
print SendTestNotificationRequestDto.to_json()

# convert the object into a dict
send_test_notification_request_dto_dict = send_test_notification_request_dto_instance.to_dict()
# create an instance of SendTestNotificationRequestDto from a dict
send_test_notification_request_dto_form_dict = send_test_notification_request_dto.from_dict(send_test_notification_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


