# GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**by_email** | **bool** |  | [optional] 
**thresholds** | [**GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds**](GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds.md) |  | [optional] 

## Example

```python
from sailpoint.v2.models.get_org_settings200_response_system_notification_config_notifications_inner import GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner from a JSON string
get_org_settings200_response_system_notification_config_notifications_inner_instance = GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner.from_json(json)
# print the JSON string representation of the object
print GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner.to_json()

# convert the object into a dict
get_org_settings200_response_system_notification_config_notifications_inner_dict = get_org_settings200_response_system_notification_config_notifications_inner_instance.to_dict()
# create an instance of GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner from a dict
get_org_settings200_response_system_notification_config_notifications_inner_form_dict = get_org_settings200_response_system_notification_config_notifications_inner.from_dict(get_org_settings200_response_system_notification_config_notifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


