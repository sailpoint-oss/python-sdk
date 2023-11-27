# GetIdentity200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**alias** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**encryption_key** | **object** |  | [optional] 
**encryption_check** | **object** |  | [optional] 
**status** | **str** |  | [optional] 
**pending** | **bool** |  | [optional] 
**password_reset_since_last_login** | **bool** |  | [optional] 
**usage_cert_attested** | **object** |  | [optional] 
**user_flags** | **object** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**alt_auth_via** | **str** |  | [optional] 
**alt_auth_via_integration_data** | **object** |  | [optional] 
**kba_answers** | **float** |  | [optional] 
**disable_password_reset** | **bool** |  | [optional] 
**pta_source_id** | **object** |  | [optional] 
**supports_password_push** | **bool** |  | [optional] 
**attributes** | **object** |  | [optional] 
**external_id** | **str** |  | [optional] 
**role** | **List[object]** |  | [optional] 
**phone** | **object** |  | [optional] 
**email** | **str** |  | [optional] 
**personal_email** | **object** |  | [optional] 
**employee_number** | **object** |  | [optional] 
**risk_score** | **float** |  | [optional] 
**feature_flags** | **object** |  | [optional] 
**feature** | **List[str]** |  | [optional] 
**org_encryption_key** | **str** |  | [optional] 
**org_encryption_key_id** | **str** |  | [optional] 
**meta** | **object** |  | [optional] 
**org** | [**GetIdentity200ResponseOrg**](GetIdentity200ResponseOrg.md) |  | [optional] 
**step_up_auth** | **bool** |  | [optional] 
**bx_install_prompted** | **bool** |  | [optional] 
**federated_login** | **bool** |  | [optional] 
**auth** | [**GetIdentity200ResponseAuth**](GetIdentity200ResponseAuth.md) |  | [optional] 
**on_network** | **bool** |  | [optional] 
**on_trusted_geo** | **bool** |  | [optional] 
**login_url** | **str** |  | [optional] 

## Example

```python
from sailpoint.cc.models.get_identity200_response import GetIdentity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIdentity200Response from a JSON string
get_identity200_response_instance = GetIdentity200Response.from_json(json)
# print the JSON string representation of the object
print GetIdentity200Response.to_json()

# convert the object into a dict
get_identity200_response_dict = get_identity200_response_instance.to_dict()
# create an instance of GetIdentity200Response from a dict
get_identity200_response_form_dict = get_identity200_response.from_dict(get_identity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


