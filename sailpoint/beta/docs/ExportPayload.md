# ExportPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional user defined description/name for export job. | [optional] 
**exclude_types** | **List[str]** | Object type names to be excluded from an sp-config export command. | [optional] 
**include_types** | **List[str]** | Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes. | [optional] 
**object_options** | [**Dict[str, ObjectExportImportOptions]**](ObjectExportImportOptions.md) | Additional options targeting specific objects related to each item in the includeTypes field | [optional] 

## Example

```python
from sailpoint.beta.models.export_payload import ExportPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPayload from a JSON string
export_payload_instance = ExportPayload.from_json(json)
# print the JSON string representation of the object
print ExportPayload.to_json()

# convert the object into a dict
export_payload_dict = export_payload_instance.to_dict()
# create an instance of ExportPayload from a dict
export_payload_form_dict = export_payload.from_dict(export_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


