# FormElementDataSourceConfigOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label is the main label to display to the user when selecting this option | [optional] 
**sub_label** | **str** | SubLabel is the sub label to display below the label in diminutive styling to help describe or identify this option | [optional] 
**value** | **str** | Value is the value to save as an entry when the user selects this option | [optional] 

## Example

```python
from sailpoint.beta.models.form_element_data_source_config_options import FormElementDataSourceConfigOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FormElementDataSourceConfigOptions from a JSON string
form_element_data_source_config_options_instance = FormElementDataSourceConfigOptions.from_json(json)
# print the JSON string representation of the object
print(FormElementDataSourceConfigOptions.to_json())

# convert the object into a dict
form_element_data_source_config_options_dict = form_element_data_source_config_options_instance.to_dict()
# create an instance of FormElementDataSourceConfigOptions from a dict
form_element_data_source_config_options_from_dict = FormElementDataSourceConfigOptions.from_dict(form_element_data_source_config_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


