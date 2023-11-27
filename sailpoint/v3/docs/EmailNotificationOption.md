# EmailNotificationOption

This is used for representing email configuration for a lifecycle state

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_managers** | **bool** | If true, then the manager is notified of the lifecycle state change. | [optional] 
**notify_all_admins** | **bool** | If true, then all the admins are notified of the lifecycle state change. | [optional] 
**notify_specific_users** | **bool** | If true, then the users specified in \&quot;emailAddressList\&quot; below are notified of lifecycle state change. | [optional] 
**email_address_list** | **List[str]** | List of user email addresses. If \&quot;notifySpecificUsers\&quot; option is true, then these users are notified of lifecycle state change. | [optional] 

## Example

```python
from sailpoint.v3.models.email_notification_option import EmailNotificationOption

# TODO update the JSON string below
json = "{}"
# create an instance of EmailNotificationOption from a JSON string
email_notification_option_instance = EmailNotificationOption.from_json(json)
# print the JSON string representation of the object
print EmailNotificationOption.to_json()

# convert the object into a dict
email_notification_option_dict = email_notification_option_instance.to_dict()
# create an instance of EmailNotificationOption from a dict
email_notification_option_form_dict = email_notification_option.from_dict(email_notification_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


