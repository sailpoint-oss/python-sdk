# PasswordPolicyHoldersDtoAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attr** | [**List[PasswordPolicyHoldersDtoAttributesIdentityAttrInner]**](PasswordPolicyHoldersDtoAttributesIdentityAttrInner.md) | Attributes of PasswordPolicyHoldersDto | [optional] 

## Example

```python
from sailpoint.v2024.models.password_policy_holders_dto_attributes import PasswordPolicyHoldersDtoAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyHoldersDtoAttributes from a JSON string
password_policy_holders_dto_attributes_instance = PasswordPolicyHoldersDtoAttributes.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyHoldersDtoAttributes.to_json())

# convert the object into a dict
password_policy_holders_dto_attributes_dict = password_policy_holders_dto_attributes_instance.to_dict()
# create an instance of PasswordPolicyHoldersDtoAttributes from a dict
password_policy_holders_dto_attributes_from_dict = PasswordPolicyHoldersDtoAttributes.from_dict(password_policy_holders_dto_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


