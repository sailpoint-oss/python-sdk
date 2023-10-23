# ObjectImportResult

Response model for import of a single object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infos** | [**List[SpConfigMessage]**](SpConfigMessage.md) | Informational messages returned from the target service on import. | 
**warnings** | [**List[SpConfigMessage]**](SpConfigMessage.md) | Warning messages returned from the target service on import. | 
**errors** | [**List[SpConfigMessage]**](SpConfigMessage.md) | Error messages returned from the target service on import. | 
**imported_objects** | [**List[BaseReferenceDto1]**](BaseReferenceDto1.md) | References to objects that were created or updated by the import. | 

## Example

```python
from beta.models.object_import_result import ObjectImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectImportResult from a JSON string
object_import_result_instance = ObjectImportResult.from_json(json)
# print the JSON string representation of the object
print ObjectImportResult.to_json()

# convert the object into a dict
object_import_result_dict = object_import_result_instance.to_dict()
# create an instance of ObjectImportResult from a dict
object_import_result_form_dict = object_import_result.from_dict(object_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


