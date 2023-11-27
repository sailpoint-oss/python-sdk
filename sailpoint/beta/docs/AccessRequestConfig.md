# AccessRequestConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals_must_be_external** | **bool** | If true, then approvals must be processed by external system. | [optional] 
**auto_approval_enabled** | **bool** | If true and requester and reviewer are the same, then automatically approve the approval. | [optional] 
**request_on_behalf_of_config** | [**RequestOnBehalfOfConfig**](RequestOnBehalfOfConfig.md) |  | [optional] 
**approval_reminder_and_escalation_config** | [**ApprovalReminderAndEscalationConfig**](ApprovalReminderAndEscalationConfig.md) |  | [optional] 
**entitlement_request_config** | [**EntitlementRequestConfig1**](EntitlementRequestConfig1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.access_request_config import AccessRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestConfig from a JSON string
access_request_config_instance = AccessRequestConfig.from_json(json)
# print the JSON string representation of the object
print AccessRequestConfig.to_json()

# convert the object into a dict
access_request_config_dict = access_request_config_instance.to_dict()
# create an instance of AccessRequestConfig from a dict
access_request_config_form_dict = access_request_config.from_dict(access_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


