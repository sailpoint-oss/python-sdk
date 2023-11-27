# UpdateOrgSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_codes** | **List[str]** |  | [optional] 
**enable_external_password_change** | **bool** |  | [optional] 
**enable_automatic_password_replay** | **bool** |  | [optional] 
**enable_automation_generation** | **bool** |  | [optional] 
**kba_req_answers** | **int** |  | [optional] 
**kba_req_for_authn** | **int** |  | [optional] 
**lockout_attempt_threshold** | **int** |  | [optional] 
**lockout_time_minutes** | **int** |  | [optional] 
**login_url** | **str** |  | [optional] 
**netmasks** | **List[str]** |  | [optional] 
**notify_authentication_setting_change** | **bool** |  | [optional] 
**password_replay_state** | **str** |  | [optional] 
**preferred_identity_invite_template** | **str** |  | [optional] 
**redirect_patterns** | **List[str]** |  | [optional] 
**sso_partner_source** | **str** |  | [optional] 
**system_notification_emails** | **List[str]** |  | [optional] 
**track_analytics** | **bool** |  | [optional] 
**usage_cert_required** | **bool** |  | [optional] 
**usage_cert_text** | **str** |  | [optional] 
**username_empty_text** | **str** |  | [optional] 
**username_label** | **str** |  | [optional] 
**white_list** | **bool** |  | [optional] 
**approval_config** | [**GetOrgSettings200ResponseApprovalConfig**](GetOrgSettings200ResponseApprovalConfig.md) |  | [optional] 

## Example

```python
from sailpoint.v2.models.update_org_settings_request import UpdateOrgSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgSettingsRequest from a JSON string
update_org_settings_request_instance = UpdateOrgSettingsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateOrgSettingsRequest.to_json()

# convert the object into a dict
update_org_settings_request_dict = update_org_settings_request_instance.to_dict()
# create an instance of UpdateOrgSettingsRequest from a dict
update_org_settings_request_form_dict = update_org_settings_request.from_dict(update_org_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


