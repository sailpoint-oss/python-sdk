# PublicIdentityAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The attribute key | [optional] 
**name** | **str** | Human-readable display name of the attribute | [optional] 
**value** | **str** | The attribute value | [optional] 

## Example

```python
from sailpoint.v2024.models.public_identity_attributes_inner import PublicIdentityAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIdentityAttributesInner from a JSON string
public_identity_attributes_inner_instance = PublicIdentityAttributesInner.from_json(json)
# print the JSON string representation of the object
print(PublicIdentityAttributesInner.to_json())

# convert the object into a dict
public_identity_attributes_inner_dict = public_identity_attributes_inner_instance.to_dict()
# create an instance of PublicIdentityAttributesInner from a dict
public_identity_attributes_inner_from_dict = PublicIdentityAttributesInner.from_dict(public_identity_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


