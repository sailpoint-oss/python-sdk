# ObjectExportImportNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_names** | **List[str]** | Object names to be included in a backup. | [optional] 

## Example

```python
from sailpoint.v2024.models.object_export_import_names import ObjectExportImportNames

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectExportImportNames from a JSON string
object_export_import_names_instance = ObjectExportImportNames.from_json(json)
# print the JSON string representation of the object
print(ObjectExportImportNames.to_json())

# convert the object into a dict
object_export_import_names_dict = object_export_import_names_instance.to_dict()
# create an instance of ObjectExportImportNames from a dict
object_export_import_names_from_dict = ObjectExportImportNames.from_dict(object_export_import_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


