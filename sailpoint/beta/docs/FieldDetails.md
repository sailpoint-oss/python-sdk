# FieldDetails


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
from sailpoint.beta.models.field_details import FieldDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FieldDetails from a JSON string
field_details_instance = FieldDetails.from_json(json)
# print the JSON string representation of the object
print FieldDetails.to_json()

# convert the object into a dict
field_details_dict = field_details_instance.to_dict()
# create an instance of FieldDetails from a dict
field_details_form_dict = field_details.from_dict(field_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


