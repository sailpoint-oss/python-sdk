# IdentityAttributeTransform

Defines a transformation definition for an identity attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attribute_name** | **str** | Name of the identity attribute. | [optional] 
**transform_definition** | [**TransformDefinition**](TransformDefinition.md) |  | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_attribute_transform import IdentityAttributeTransform

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttributeTransform from a JSON string
identity_attribute_transform_instance = IdentityAttributeTransform.from_json(json)
# print the JSON string representation of the object
print IdentityAttributeTransform.to_json()

# convert the object into a dict
identity_attribute_transform_dict = identity_attribute_transform_instance.to_dict()
# create an instance of IdentityAttributeTransform from a dict
identity_attribute_transform_form_dict = identity_attribute_transform.from_dict(identity_attribute_transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


