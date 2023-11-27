# AuthUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** | Tenant name. | [optional] 
**id** | **str** | Identity ID. | [optional] 
**uid** | **str** | Identity unique identitifier. | [optional] 
**profile** | **str** | ID of the auth profile associated with this auth user. | [optional] 
**identification_number** | **str** | Auth user employee number. | [optional] 
**email** | **str** | Auth user&#39;s email. | [optional] 
**phone** | **str** | Auth user&#39;s phone number. | [optional] 
**work_phone** | **str** | Auth user&#39;s work phone number. | [optional] 
**personal_email** | **str** | Auth user&#39;s personal email. | [optional] 
**firstname** | **str** | Auth user&#39;s first name. | [optional] 
**lastname** | **str** | Auth user&#39;s last name. | [optional] 
**display_name** | **str** | Auth user&#39;s name in displayed format. | [optional] 
**alias** | **str** | Auth user&#39;s alias. | [optional] 
**last_password_change_date** | **str** | the date of last password change | [optional] 
**last_login_timestamp** | **int** | Timestamp of the last login (long type value). | [optional] 
**current_login_timestamp** | **int** | Timestamp of the current login (long type value). | [optional] 
**capabilities** | **List[str]** | Array of capabilities for this auth user. | [optional] 

## Example

```python
from sailpoint.v3.models.auth_user import AuthUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthUser from a JSON string
auth_user_instance = AuthUser.from_json(json)
# print the JSON string representation of the object
print AuthUser.to_json()

# convert the object into a dict
auth_user_dict = auth_user_instance.to_dict()
# create an instance of AuthUser from a dict
auth_user_form_dict = auth_user.from_dict(auth_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


