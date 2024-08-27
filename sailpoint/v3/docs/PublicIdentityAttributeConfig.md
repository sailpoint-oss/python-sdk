# PublicIdentityAttributeConfig

Used to map an attribute key for an Identity to its display name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | The attribute display name | [optional] 

## Example

```python
from sailpoint.v3.models.public_identity_attribute_config import PublicIdentityAttributeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIdentityAttributeConfig from a JSON string
public_identity_attribute_config_instance = PublicIdentityAttributeConfig.from_json(json)
# print the JSON string representation of the object
print(PublicIdentityAttributeConfig.to_json())

# convert the object into a dict
public_identity_attribute_config_dict = public_identity_attribute_config_instance.to_dict()
# create an instance of PublicIdentityAttributeConfig from a dict
public_identity_attribute_config_from_dict = PublicIdentityAttributeConfig.from_dict(public_identity_attribute_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


