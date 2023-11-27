# IdentityAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The technical name of the identity attribute | [optional] 
**display_name** | **str** | The business-friendly name of the identity attribute | [optional] 
**standard** | **bool** | Shows if the attribute is &#39;standard&#39; or default | [optional] [default to False]
**type** | **str** | The type of the identity attribute | [optional] 
**multi** | **bool** | Shows if the identity attribute is multi-valued | [optional] [default to False]
**searchable** | **bool** | Shows if the identity attribute is searchable | [optional] [default to False]
**system** | **bool** | Shows this is &#39;system&#39; identity attribute that does not have a source and is not configurable. | [optional] [default to False]
**sources** | [**List[Source1]**](Source1.md) | List of sources for an attribute, this specifies how the value of the rule is derived | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute import IdentityAttribute

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


