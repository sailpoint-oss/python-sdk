# FieldDetailsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attribute. | [optional] 
**transform** | **object** | The transform to apply to the field | [optional] 
**attributes** | **object** | Attributes required for the transform | [optional] 
**is_required** | **bool** | Flag indicating whether or not the attribute is required. | [optional] [readonly] [default to False]
**type** | **str** | The type of the attribute. | [optional] 
**is_multi_valued** | **bool** | Flag indicating whether or not the attribute is multi-valued. | [optional] [default to False]

## Example

```python
from beta.models.field_details_dto import FieldDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDetailsDto from a JSON string
field_details_dto_instance = FieldDetailsDto.from_json(json)
# print the JSON string representation of the object
print FieldDetailsDto.to_json()

# convert the object into a dict
field_details_dto_dict = field_details_dto_instance.to_dict()
# create an instance of FieldDetailsDto from a dict
field_details_dto_form_dict = field_details_dto.from_dict(field_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


