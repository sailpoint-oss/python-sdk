# AttributeValueDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Technical name of the Attribute value. This is unique and cannot be changed after creation. | [optional] 
**name** | **str** | The display name of the Attribute value. | [optional] 
**status** | **str** | The status of the Attribute value. | [optional] 

## Example

```python
from sailpoint.beta.models.attribute_value_dto import AttributeValueDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeValueDTO from a JSON string
attribute_value_dto_instance = AttributeValueDTO.from_json(json)
# print the JSON string representation of the object
print AttributeValueDTO.to_json()

# convert the object into a dict
attribute_value_dto_dict = attribute_value_dto_instance.to_dict()
# create an instance of AttributeValueDTO from a dict
attribute_value_dto_form_dict = attribute_value_dto.from_dict(attribute_value_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


