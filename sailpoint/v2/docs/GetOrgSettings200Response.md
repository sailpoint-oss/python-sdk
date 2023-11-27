# GetOrgSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**script_name** | **str** |  | [optional] 
**sso_domain** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**max_registered_identities** | **int** |  | [optional] 
**identity_count** | **int** |  | [optional] 
**kba_req_for_authn** | **int** |  | [optional] 
**kba_req_answers** | **int** |  | [optional] 
**lockout_attempt_threshold** | **int** |  | [optional] 
**lockout_time_minutes** | **int** |  | [optional] 
**usage_cert_required** | **bool** |  | [optional] 
**admin_strong_auth_required** | **bool** |  | [optional] 
**enable_external_password_change** | **bool** |  | [optional] 
**enable_password_replay** | **bool** |  | [optional] 
**enable_automatic_password_replay** | **bool** |  | [optional] 
**netmasks** | **List[str]** |  | [optional] 
**country_codes** | **List[str]** |  | [optional] 
**white_list** | **bool** |  | [optional] 
**email_test_mode** | **bool** |  | [optional] 
**email_test_address** | **str** |  | [optional] 
**username_empty_text** | **str** |  | [optional] 
**username_label** | **str** |  | [optional] 
**enable_automation_generation** | **bool** |  | [optional] 
**password_replay_state** | **str** |  | [optional] 
**system_notification_config** | [**GetOrgSettings200ResponseSystemNotificationConfig**](GetOrgSettings200ResponseSystemNotificationConfig.md) |  | [optional] 
**system_notification_emails** | **List[str]** |  | [optional] 
**login_url** | **str** |  | [optional] 
**redirect_patterns** | **List[str]** |  | [optional] 
**style_hash** | **str** |  | [optional] 
**approval_config** | [**GetOrgSettings200ResponseApprovalConfig**](GetOrgSettings200ResponseApprovalConfig.md) |  | [optional] 
**sso_partner_source** | **str** |  | [optional] 

## Example

```python
from sailpoint.v2.models.get_org_settings200_response import GetOrgSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrgSettings200Response from a JSON string
get_org_settings200_response_instance = GetOrgSettings200Response.from_json(json)
# print the JSON string representation of the object
print GetOrgSettings200Response.to_json()

# convert the object into a dict
get_org_settings200_response_dict = get_org_settings200_response_instance.to_dict()
# create an instance of GetOrgSettings200Response from a dict
get_org_settings200_response_form_dict = get_org_settings200_response.from_dict(get_org_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


