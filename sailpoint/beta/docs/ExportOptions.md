# ExportOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_types** | **List[str]** | Object type names to be excluded from an sp-config export command. | [optional] 
**include_types** | **List[str]** | Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes. | [optional] 
**object_options** | [**Dict[str, ObjectExportImportOptions]**](ObjectExportImportOptions.md) | Additional options targeting specific objects related to each item in the includeTypes field | [optional] 

## Example

```python
from sailpoint.beta.models.export_options import ExportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ExportOptions from a JSON string
export_options_instance = ExportOptions.from_json(json)
# print the JSON string representation of the object
print ExportOptions.to_json()

# convert the object into a dict
export_options_dict = export_options_instance.to_dict()
# create an instance of ExportOptions from a dict
export_options_form_dict = export_options.from_dict(export_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


