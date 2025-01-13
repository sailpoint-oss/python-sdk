# PasswordPolicyHoldersDtoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The password policy Id. | [optional] 
**policy_name** | **str** | The name of the password policy. | [optional] 
**selectors** | [**PasswordPolicyHoldersDtoAttributes**](.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.password_policy_holders_dto_inner import PasswordPolicyHoldersDtoInner

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyHoldersDtoInner from a JSON string
password_policy_holders_dto_inner_instance = PasswordPolicyHoldersDtoInner.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyHoldersDtoInner.to_json())

# convert the object into a dict
password_policy_holders_dto_inner_dict = password_policy_holders_dto_inner_instance.to_dict()
# create an instance of PasswordPolicyHoldersDtoInner from a dict
password_policy_holders_dto_inner_from_dict = PasswordPolicyHoldersDtoInner.from_dict(password_policy_holders_dto_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


