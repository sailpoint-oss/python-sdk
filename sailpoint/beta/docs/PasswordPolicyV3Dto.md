# PasswordPolicyV3Dto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The password policy Id. | [optional] 
**description** | **str** | Description for current password policy. | [optional] 
**name** | **str** | The name of the password policy. | [optional] 
**date_crated** | **datetime** | Date the Password Policy was created. | [optional] 
**last_updated** | **datetime** | Date the Password Policy was updated. | [optional] 
**first_expiration_reminder** | **int** | The number of days before expiration remaninder. | [optional] 
**account_id_min_word_length** | **int** | The minimun length of account Id. By default is equals to -1. | [optional] 
**account_name_min_word_length** | **int** | The minimun length of account name. By default is equals to -1. | [optional] 
**min_alpha** | **int** | Maximum alpha. By default is equals to 0. | [optional] 
**min_character_types** | **int** | MinCharacterTypes. By default is equals to -1. | [optional] 
**max_length** | **int** | Maximum length of the password. | [optional] 
**min_length** | **int** | Minimum length of the password. By default is equals to 0. | [optional] 
**max_repeated_chars** | **int** | Maximum repetition of the same character in the password. By default is equals to -1. | [optional] 
**min_lower** | **int** | Minimum amount of lower case character in the password. By default is equals to 0. | [optional] 
**min_numeric** | **int** | Minimum amount of numeric characters in the password. By default is equals to 0. | [optional] 
**min_special** | **int** | Minimum amount of special symbols in the password. By default is equals to 0. | [optional] 
**min_upper** | **int** | Minimum amount of upper case symbols in the password. By default is equals to 0. | [optional] 
**password_expiration** | **int** | Number of days before current password expires. By default is equals to 90. | [optional] 
**default_policy** | **bool** | Defines whether this policy is default or not. Default policy is created automatically when an org is setup. This field is false by default. | [optional] [default to False]
**enable_passwd_expiration** | **bool** | Defines whether this policy is enabled to expire or not. This field is false by default. | [optional] [default to False]
**require_strong_authn** | **bool** | Defines whether this policy require strong Auth or not. This field is false by default. | [optional] [default to False]
**require_strong_auth_off_network** | **bool** | Defines whether this policy require strong Auth of network or not. This field is false by default. | [optional] [default to False]
**require_strong_auth_untrusted_geographies** | **bool** | Defines whether this policy require strong Auth for untrusted geographies. This field is false by default. | [optional] [default to False]
**use_account_attributes** | **bool** | Defines whether this policy uses account attributes or not. This field is false by default. | [optional] [default to False]
**use_dictionary** | **bool** | Defines whether this policy uses dictionary or not. This field is false by default. | [optional] [default to False]
**use_identity_attributes** | **bool** | Defines whether this policy uses identity attributes or not. This field is false by default. | [optional] [default to False]
**validate_against_account_id** | **bool** | Defines whether this policy validate against account id or not. This field is false by default. | [optional] [default to False]
**validate_against_account_name** | **bool** | Defines whether this policy validate against account name or not. This field is false by default. | [optional] [default to False]
**source_ids** | **List[str]** | List of sources IDs managed by this password policy. | [optional] 

## Example

```python
from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyV3Dto from a JSON string
password_policy_v3_dto_instance = PasswordPolicyV3Dto.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyV3Dto.to_json()

# convert the object into a dict
password_policy_v3_dto_dict = password_policy_v3_dto_instance.to_dict()
# create an instance of PasswordPolicyV3Dto from a dict
password_policy_v3_dto_form_dict = password_policy_v3_dto.from_dict(password_policy_v3_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


