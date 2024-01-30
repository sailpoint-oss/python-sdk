# PublicIdentityConfig

Details of up to 5 Identity attributes that will be publicly accessible for all Identities to anyone in the org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[PublicIdentityAttributeConfig]**](PublicIdentityAttributeConfig.md) | Up to 5 identity attributes that will be available to everyone in the org for all users in the org. | [optional] 
**modified** | **datetime** | When this configuration was last modified. | [optional] 
**modified_by** | [**IdentityReference**](IdentityReference.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.public_identity_config import PublicIdentityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIdentityConfig from a JSON string
public_identity_config_instance = PublicIdentityConfig.from_json(json)
# print the JSON string representation of the object
print PublicIdentityConfig.to_json()

# convert the object into a dict
public_identity_config_dict = public_identity_config_instance.to_dict()
# create an instance of PublicIdentityConfig from a dict
public_identity_config_form_dict = public_identity_config.from_dict(public_identity_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


