# GetApplication200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_app_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**app_center_enabled** | **bool** |  | [optional] 
**provision_request_enabled** | **bool** |  | [optional] 
**control_type** | **str** |  | [optional] 
**mobile** | **bool** |  | [optional] 
**private_app** | **bool** |  | [optional] 
**script_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**health** | [**ListApplications200ResponseInnerHealth**](ListApplications200ResponseInnerHealth.md) |  | [optional] 
**enable_sso** | **bool** |  | [optional] 
**sso_method** | **str** |  | [optional] 
**has_links** | **bool** |  | [optional] 
**has_automations** | **bool** |  | [optional] 
**step_up_auth_data** | **object** |  | [optional] 
**step_up_auth_type** | **str** |  | [optional] 
**usage_analytics** | **bool** |  | [optional] 
**usage_cert_required** | **bool** |  | [optional] 
**usage_cert_text** | **object** |  | [optional] 
**launchpad_enabled** | **bool** |  | [optional] 
**password_managed** | **bool** |  | [optional] 
**owner** | [**ListApplications200ResponseInnerOwner**](ListApplications200ResponseInnerOwner.md) |  | [optional] 
**date_created** | **float** |  | [optional] 
**last_updated** | **float** |  | [optional] 
**default_access_profile** | **object** |  | [optional] 
**service** | **str** |  | [optional] 
**selected_sso_method** | **str** |  | [optional] 
**supported_sso_methods** | **float** |  | [optional] 
**off_network_blocked_roles** | **object** |  | [optional] 
**supported_off_network** | **str** |  | [optional] 
**account_service_id** | **float** |  | [optional] 
**launcher_count** | **float** |  | [optional] 
**account_service_name** | **str** |  | [optional] 
**account_service_external_id** | **str** |  | [optional] 
**account_service_match_all_accounts** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**account_service_use_for_password_management** | **bool** |  | [optional] 
**account_service_policy_id** | **str** |  | [optional] 
**account_service_policy_name** | **str** |  | [optional] 
**require_strong_authn** | **bool** |  | [optional] 
**account_service_policies** | [**List[ListApplications200ResponseInnerAccountServicePoliciesInner]**](ListApplications200ResponseInnerAccountServicePoliciesInner.md) |  | [optional] 
**xsd_version** | **str** |  | [optional] 
**app_profiles** | [**List[ListApplications200ResponseInnerAppProfilesInner]**](ListApplications200ResponseInnerAppProfilesInner.md) |  | [optional] 
**password_service_id** | **float** |  | [optional] 
**access_profile_ids** | **object** |  | [optional] 

## Example

```python
from cc.models.get_application200_response import GetApplication200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplication200Response from a JSON string
get_application200_response_instance = GetApplication200Response.from_json(json)
# print the JSON string representation of the object
print GetApplication200Response.to_json()

# convert the object into a dict
get_application200_response_dict = get_application200_response_instance.to_dict()
# create an instance of GetApplication200Response from a dict
get_application200_response_form_dict = get_application200_response.from_dict(get_application200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


