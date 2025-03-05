# ExportOptions1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_types** | **List[str]** | Object type names to be excluded from an sp-config export command. | [optional] 
**include_types** | **List[str]** | Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes. | [optional] 
**object_options** | [**Dict[str, ObjectExportImportOptions]**](ObjectExportImportOptions.md) | Additional options targeting specific objects related to each item in the includeTypes field | [optional] 

## Example

```python
from sailpoint.v2024.models.export_options1 import ExportOptions1

# TODO update the JSON string below
json = "{}"
# create an instance of ExportOptions1 from a JSON string
export_options1_instance = ExportOptions1.from_json(json)
# print the JSON string representation of the object
print(ExportOptions1.to_json())

# convert the object into a dict
export_options1_dict = export_options1_instance.to_dict()
# create an instance of ExportOptions1 from a dict
export_options1_from_dict = ExportOptions1.from_dict(export_options1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


