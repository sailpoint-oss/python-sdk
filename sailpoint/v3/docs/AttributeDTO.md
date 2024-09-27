# AttributeDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Technical name of the Attribute. This is unique and cannot be changed after creation. | [optional] 
**name** | **str** | The display name of the key. | [optional] 
**multiselect** | **bool** | Indicates whether the attribute can have multiple values. | [optional] [default to False]
**status** | **str** | The status of the Attribute. | [optional] 
**type** | **str** | The type of the Attribute. This can be either \&quot;custom\&quot; or \&quot;governance\&quot;. | [optional] 
**object_types** | **List[str]** | An array of object types this attributes values can be applied to. Possible values are \&quot;all\&quot; or \&quot;entitlement\&quot;. Value \&quot;all\&quot; means this attribute can be used with all object types that are supported. | [optional] 
**description** | **str** | The description of the Attribute. | [optional] 
**values** | [**List[AttributeValueDTO]**](AttributeValueDTO.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.attribute_dto import AttributeDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDTO from a JSON string
attribute_dto_instance = AttributeDTO.from_json(json)
# print the JSON string representation of the object
print(AttributeDTO.to_json())

# convert the object into a dict
attribute_dto_dict = attribute_dto_instance.to_dict()
# create an instance of AttributeDTO from a dict
attribute_dto_from_dict = AttributeDTO.from_dict(attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


