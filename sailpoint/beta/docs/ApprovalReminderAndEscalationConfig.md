# ApprovalReminderAndEscalationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_until_escalation** | **int** | Number of days to wait before the first reminder. If no reminders are configured, then this is the number of days to wait before escalation. | [optional] 
**days_between_reminders** | **int** | Number of days to wait between reminder notifications. | [optional] 
**max_reminders** | **int** | Maximum number of reminder notification to send to the reviewer before approval escalation. | [optional] 
**fallback_approver_ref** | [**IdentityReferenceWithNameAndEmail**](IdentityReferenceWithNameAndEmail.md) |  | [optional] 

## Example

```python
from beta.models.approval_reminder_and_escalation_config import ApprovalReminderAndEscalationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalReminderAndEscalationConfig from a JSON string
approval_reminder_and_escalation_config_instance = ApprovalReminderAndEscalationConfig.from_json(json)
# print the JSON string representation of the object
print ApprovalReminderAndEscalationConfig.to_json()

# convert the object into a dict
approval_reminder_and_escalation_config_dict = approval_reminder_and_escalation_config_instance.to_dict()
# create an instance of ApprovalReminderAndEscalationConfig from a dict
approval_reminder_and_escalation_config_form_dict = approval_reminder_and_escalation_config.from_dict(approval_reminder_and_escalation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


