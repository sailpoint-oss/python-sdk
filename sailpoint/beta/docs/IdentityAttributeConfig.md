# IdentityAttributeConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If the profile or mapping is enabled | [optional] [default to True]
**attribute_transforms** | [**List[IdentityAttributeTransform]**](IdentityAttributeTransform.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute_config import IdentityAttributeConfig

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


