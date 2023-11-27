# ObjectExportImportOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_ids** | **List[str]** | Object ids to be included in an import or export. | [optional] 
**included_names** | **List[str]** | Object names to be included in an import or export. | [optional] 

## Example

```python
from sailpoint.beta.models.object_export_import_options import ObjectExportImportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectExportImportOptions from a JSON string
object_export_import_options_instance = ObjectExportImportOptions.from_json(json)
# print the JSON string representation of the object
print ObjectExportImportOptions.to_json()

# convert the object into a dict
object_export_import_options_dict = object_export_import_options_instance.to_dict()
# create an instance of ObjectExportImportOptions from a dict
object_export_import_options_form_dict = object_export_import_options.from_dict(object_export_import_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


