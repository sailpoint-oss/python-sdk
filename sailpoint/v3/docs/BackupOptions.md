# BackupOptions

Backup options control what will be included in the backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_types** | **List[str]** | Object type names to be included in a Configuration Hub backup command. | [optional] 
**object_options** | [**Dict[str, ObjectExportImportNames]**](ObjectExportImportNames.md) | Additional options targeting specific objects related to each item in the includeTypes field. | [optional] 

## Example

```python
from sailpoint.v3.models.backup_options import BackupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BackupOptions from a JSON string
backup_options_instance = BackupOptions.from_json(json)
# print the JSON string representation of the object
print(BackupOptions.to_json())

# convert the object into a dict
backup_options_dict = backup_options_instance.to_dict()
# create an instance of BackupOptions from a dict
backup_options_from_dict = BackupOptions.from_dict(backup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


