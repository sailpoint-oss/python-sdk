# IdentityAttributeTransform1

Defines a transformation definition for an identity attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attribute_name** | **str** | Name of the identity attribute. | [optional] 
**transform_definition** | [**TransformDefinition1**](TransformDefinition1.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute_transform1 import IdentityAttributeTransform1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributeTransform1 from a JSON string
identity_attribute_transform1_instance = IdentityAttributeTransform1.from_json(json)
# print the JSON string representation of the object
print(IdentityAttributeTransform1.to_json())

# convert the object into a dict
identity_attribute_transform1_dict = identity_attribute_transform1_instance.to_dict()
# create an instance of IdentityAttributeTransform1 from a dict
identity_attribute_transform1_from_dict = IdentityAttributeTransform1.from_dict(identity_attribute_transform1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


