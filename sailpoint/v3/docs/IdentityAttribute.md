# IdentityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | Human-readable display name of the attribute | [optional] 
**value** | **str** | The attribute value | [optional] 

## Example

```python
from sailpoint.v3.models.identity_attribute import IdentityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttribute from a JSON string
identity_attribute_instance = IdentityAttribute.from_json(json)
# print the JSON string representation of the object
print IdentityAttribute.to_json()

# convert the object into a dict
identity_attribute_dict = identity_attribute_instance.to_dict()
# create an instance of IdentityAttribute from a dict
identity_attribute_form_dict = identity_attribute.from_dict(identity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


