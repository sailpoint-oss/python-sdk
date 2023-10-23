# IdentityAttributeConfig

Defines all the identity attribute mapping configurations. This defines how to generate or collect data for each identity attributes in identity refresh process.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The backend will only promote values if the profile/mapping is enabled. | [optional] [default to False]
**attribute_transforms** | [**List[IdentityAttributeTransform]**](IdentityAttributeTransform.md) |  | [optional] 

## Example

```python
from v3.models.identity_attribute_config import IdentityAttributeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributeConfig from a JSON string
identity_attribute_config_instance = IdentityAttributeConfig.from_json(json)
# print the JSON string representation of the object
print IdentityAttributeConfig.to_json()

# convert the object into a dict
identity_attribute_config_dict = identity_attribute_config_instance.to_dict()
# create an instance of IdentityAttributeConfig from a dict
identity_attribute_config_form_dict = identity_attribute_config.from_dict(identity_attribute_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


