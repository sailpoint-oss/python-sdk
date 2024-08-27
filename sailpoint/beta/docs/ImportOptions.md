# ImportOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_types** | **List[str]** | Object type names to be excluded from an sp-config export command. | [optional] 
**include_types** | **List[str]** | Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes. | [optional] 
**object_options** | [**Dict[str, ObjectExportImportOptions]**](ObjectExportImportOptions.md) | Additional options targeting specific objects related to each item in the includeTypes field | [optional] 
**default_references** | **List[str]** | List of object types that can be used to resolve references on import. | [optional] 
**exclude_backup** | **bool** | By default, every import will first export all existing objects supported by sp-config as a backup before the import is attempted. If excludeBackup is true, the backup will not be performed. | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.import_options import ImportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOptions from a JSON string
import_options_instance = ImportOptions.from_json(json)
# print the JSON string representation of the object
print(ImportOptions.to_json())

# convert the object into a dict
import_options_dict = import_options_instance.to_dict()
# create an instance of ImportOptions from a dict
import_options_from_dict = ImportOptions.from_dict(import_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


