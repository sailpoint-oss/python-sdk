# IdentityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identity attribute&#39;s technical name. | 
**display_name** | **str** | Identity attribute&#39;s business-friendly name. | [optional] 
**standard** | **bool** | Indicates whether the attribute is &#39;standard&#39; or &#39;default&#39;. | [optional] [default to False]
**type** | **str** | Identity attribute&#39;s type. | [optional] 
**multi** | **bool** | Indicates whether the identity attribute is multi-valued. | [optional] [default to False]
**searchable** | **bool** | Indicates whether the identity attribute is searchable. | [optional] [default to False]
**system** | **bool** | Indicates whether the identity attribute is &#39;system&#39;, meaning that it doesn&#39;t have a source and isn&#39;t configurable. | [optional] [default to False]
**sources** | [**List[Source1]**](Source1.md) | Identity attribute&#39;s list of sources - this specifies how the rule&#39;s value is derived. | [optional] 

## Example

```python
from sailpoint.v2024.models.identity_attribute import IdentityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttribute from a JSON string
identity_attribute_instance = IdentityAttribute.from_json(json)
# print the JSON string representation of the object
print(IdentityAttribute.to_json())

# convert the object into a dict
identity_attribute_dict = identity_attribute_instance.to_dict()
# create an instance of IdentityAttribute from a dict
identity_attribute_from_dict = IdentityAttribute.from_dict(identity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


