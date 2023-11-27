# GetOrgSettings200ResponseSystemNotificationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner]**](GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner.md) |  | [optional] 
**recipient_type** | **str** |  | [optional] 

## Example

```python
from sailpoint.v2.models.get_org_settings200_response_system_notification_config import GetOrgSettings200ResponseSystemNotificationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrgSettings200ResponseSystemNotificationConfig from a JSON string
get_org_settings200_response_system_notification_config_instance = GetOrgSettings200ResponseSystemNotificationConfig.from_json(json)
# print the JSON string representation of the object
print GetOrgSettings200ResponseSystemNotificationConfig.to_json()

# convert the object into a dict
get_org_settings200_response_system_notification_config_dict = get_org_settings200_response_system_notification_config_instance.to_dict()
# create an instance of GetOrgSettings200ResponseSystemNotificationConfig from a dict
get_org_settings200_response_system_notification_config_form_dict = get_org_settings200_response_system_notification_config.from_dict(get_org_settings200_response_system_notification_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


