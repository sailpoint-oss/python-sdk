# PasswordInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**public_key_id** | **str** |  | [optional] 
**public_key** | **str** | User&#39;s public key with Base64 encoding | [optional] 
**accounts** | [**List[PasswordInfoAccount]**](PasswordInfoAccount.md) | Account info related to queried identity and source | [optional] 
**policies** | **List[str]** | Password constraints | [optional] 

## Example

```python
from sailpoint.beta.models.password_info import PasswordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordInfo from a JSON string
password_info_instance = PasswordInfo.from_json(json)
# print the JSON string representation of the object
print PasswordInfo.to_json()

# convert the object into a dict
password_info_dict = password_info_instance.to_dict()
# create an instance of PasswordInfo from a dict
password_info_form_dict = password_info.from_dict(password_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


