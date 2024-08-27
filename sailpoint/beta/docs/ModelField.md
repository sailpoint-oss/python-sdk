# ModelField


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
from sailpoint.beta.models.model_field import ModelField

# TODO update the JSON string below
json = "{}"
# create an instance of ModelField from a JSON string
model_field_instance = ModelField.from_json(json)
# print the JSON string representation of the object
print(ModelField.to_json())

# convert the object into a dict
model_field_dict = model_field_instance.to_dict()
# create an instance of ModelField from a dict
model_field_from_dict = ModelField.from_dict(model_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


