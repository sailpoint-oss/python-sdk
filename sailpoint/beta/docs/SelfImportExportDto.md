# SelfImportExportDto

Self block for imported/exported object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Imported/exported object&#39;s DTO type. Import is currently only possible with the IDENTITY_OBJECT_CONFIG, IDENTITY_PROFILE, RULE, SOURCE, TRANSFORM, and TRIGGER_SUBSCRIPTION object types. | [optional] 
**id** | **str** | Imported/exported object&#39;s ID. | [optional] 
**name** | **str** | Imported/exported object&#39;s display name. | [optional] 

## Example

```python
from beta.models.self_import_export_dto import SelfImportExportDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelfImportExportDto from a JSON string
self_import_export_dto_instance = SelfImportExportDto.from_json(json)
# print the JSON string representation of the object
print SelfImportExportDto.to_json()

# convert the object into a dict
self_import_export_dto_dict = self_import_export_dto_instance.to_dict()
# create an instance of SelfImportExportDto from a dict
self_import_export_dto_form_dict = self_import_export_dto.from_dict(self_import_export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


