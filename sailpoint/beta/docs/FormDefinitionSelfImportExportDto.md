# FormDefinitionSelfImportExportDto

Self block for imported/exported object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Imported/exported object&#39;s DTO type. | [optional] 
**id** | **str** | Imported/exported object&#39;s ID. | [optional] 
**name** | **str** | Imported/exported object&#39;s display name. | [optional] 

## Example

```python
from sailpoint.beta.models.form_definition_self_import_export_dto import FormDefinitionSelfImportExportDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormDefinitionSelfImportExportDto from a JSON string
form_definition_self_import_export_dto_instance = FormDefinitionSelfImportExportDto.from_json(json)
# print the JSON string representation of the object
print FormDefinitionSelfImportExportDto.to_json()

# convert the object into a dict
form_definition_self_import_export_dto_dict = form_definition_self_import_export_dto_instance.to_dict()
# create an instance of FormDefinitionSelfImportExportDto from a dict
form_definition_self_import_export_dto_form_dict = form_definition_self_import_export_dto.from_dict(form_definition_self_import_export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


