# Field


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the FormItem | [optional] 
**display_name** | **str** | Display name of the field | [optional] 
**display_type** | **str** | Type of the field to display | [optional] 
**required** | **bool** | True if the field is required | [optional] 
**allowed_values_list** | **List[object]** | List of allowed values for the field | [optional] 
**value** | **object** | Value of the field | [optional] 

## Example

```python
from beta.models.field import Field

# TODO update the JSON string below
json = "{}"
# create an instance of Field from a JSON string
field_instance = Field.from_json(json)
# print the JSON string representation of the object
print Field.to_json()

# convert the object into a dict
field_dict = field_instance.to_dict()
# create an instance of Field from a dict
field_form_dict = field.from_dict(field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


