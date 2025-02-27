# IdentityAttributeConfig1

Defines all the identity attribute mapping configurations. This defines how to generate or collect data for each identity attributes in identity refresh process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Backend will only promote values if the profile/mapping is enabled. | [optional] [default to False]
**attribute_transforms** | [**List[IdentityAttributeTransform1]**](IdentityAttributeTransform1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute_config1 import IdentityAttributeConfig1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributeConfig1 from a JSON string
identity_attribute_config1_instance = IdentityAttributeConfig1.from_json(json)
# print the JSON string representation of the object
print(IdentityAttributeConfig1.to_json())

# convert the object into a dict
identity_attribute_config1_dict = identity_attribute_config1_instance.to_dict()
# create an instance of IdentityAttributeConfig1 from a dict
identity_attribute_config1_from_dict = IdentityAttributeConfig1.from_dict(identity_attribute_config1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


