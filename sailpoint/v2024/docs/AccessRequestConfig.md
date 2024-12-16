# AccessRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals_must_be_external** | **bool** | If this is true, approvals must be processed by an external system. Also, if this is true, it blocks Request Center access requests and returns an error for any user who isn&#39;t an org admin. | [optional] [default to False]
**auto_approval_enabled** | **bool** | If this is true and the requester and reviewer are the same, the request is automatically approved. | [optional] [default to False]
**reauthorization_enabled** | **bool** | If this is true, reauthorization will be enforced for appropriately configured access items. Enablement of this feature is currently in a limited state. | [optional] [default to False]
**request_on_behalf_of_config** | [**RequestOnBehalfOfConfig**](RequestOnBehalfOfConfig.md) |  | [optional] 
**approval_reminder_and_escalation_config** | [**ApprovalReminderAndEscalationConfig**](ApprovalReminderAndEscalationConfig.md) |  | [optional] 
**entitlement_request_config** | [**EntitlementRequestConfig1**](EntitlementRequestConfig1.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_config import AccessRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestConfig from a JSON string
access_request_config_instance = AccessRequestConfig.from_json(json)
# print the JSON string representation of the object
print(AccessRequestConfig.to_json())

# convert the object into a dict
access_request_config_dict = access_request_config_instance.to_dict()
# create an instance of AccessRequestConfig from a dict
access_request_config_from_dict = AccessRequestConfig.from_dict(access_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


