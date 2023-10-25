# GetIdentity200ResponseOrg


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**script_name** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**num_questions** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**max_registered_users** | **float** |  | [optional] 
**pod** | **str** |  | [optional] 
**pwd_reset_personal_phone** | **bool** |  | [optional] 
**pwd_reset_personal_email** | **bool** |  | [optional] 
**pwd_reset_kba** | **bool** |  | [optional] 
**pwd_reset_email** | **bool** |  | [optional] 
**pwd_reset_duo** | **bool** |  | [optional] 
**pwd_reset_phone_mask** | **bool** |  | [optional] 
**auth_error_text** | **object** |  | [optional] 
**strong_auth_kba** | **bool** |  | [optional] 
**strong_auth_personal_phone** | **bool** |  | [optional] 
**strong_auth_personal_email** | **bool** |  | [optional] 
**integrations** | **List[object]** |  | [optional] 
**product_name** | **str** |  | [optional] 
**kba_req_for_authn** | **float** |  | [optional] 
**kba_req_answers** | **float** |  | [optional] 
**lockout_attempt_threshold** | **float** |  | [optional] 
**lockout_time_minutes** | **float** |  | [optional] 
**usage_cert_required** | **bool** |  | [optional] 
**admin_strong_auth_required** | **bool** |  | [optional] 
**enable_external_password_change** | **bool** |  | [optional] 
**enable_password_replay** | **bool** |  | [optional] 
**enable_automatic_password_replay** | **bool** |  | [optional] 
**notify_authentication_setting_change** | **bool** |  | [optional] 
**netmasks** | **object** |  | [optional] 
**country_codes** | **object** |  | [optional] 
**white_list** | **bool** |  | [optional] 
**username_empty_text** | **object** |  | [optional] 
**username_label** | **object** |  | [optional] 
**enable_automation_generation** | **bool** |  | [optional] 
**email_test_mode** | **bool** |  | [optional] 
**email_test_address** | **str** |  | [optional] 
**org_type** | **str** |  | [optional] 
**password_replay_state** | **str** |  | [optional] 
**system_notification_config** | **str** |  | [optional] 
**redirect_patterns** | **str** |  | [optional] 
**max_cluster_debug_hours** | **str** |  | [optional] 
**brand_name** | **str** |  | [optional] 
**logo** | **object** |  | [optional] 
**email_from_address** | **object** |  | [optional] 
**standard_logo_url** | **object** |  | [optional] 
**narrow_logo_url** | **object** |  | [optional] 
**action_button_color** | **str** |  | [optional] 
**active_link_color** | **str** |  | [optional] 
**navigation_color** | **str** |  | [optional] 

## Example

```python
from cc.models.get_identity200_response_org import GetIdentity200ResponseOrg

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentity200ResponseOrg from a JSON string
get_identity200_response_org_instance = GetIdentity200ResponseOrg.from_json(json)
# print the JSON string representation of the object
print GetIdentity200ResponseOrg.to_json()

# convert the object into a dict
get_identity200_response_org_dict = get_identity200_response_org_instance.to_dict()
# create an instance of GetIdentity200ResponseOrg from a dict
get_identity200_response_org_form_dict = get_identity200_response_org.from_dict(get_identity200_response_org_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


