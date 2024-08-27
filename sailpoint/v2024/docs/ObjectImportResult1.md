# ObjectImportResult1

Response model for import of a single object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infos** | [**List[SpConfigMessage1]**](SpConfigMessage1.md) | Informational messages returned from the target service on import. | 
**warnings** | [**List[SpConfigMessage1]**](SpConfigMessage1.md) | Warning messages returned from the target service on import. | 
**errors** | [**List[SpConfigMessage1]**](SpConfigMessage1.md) | Error messages returned from the target service on import. | 
**imported_objects** | [**List[ImportObject]**](ImportObject.md) | References to objects that were created or updated by the import. | 

## Example

```python
from sailpoint.v2024.models.object_import_result1 import ObjectImportResult1

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectImportResult1 from a JSON string
object_import_result1_instance = ObjectImportResult1.from_json(json)
# print the JSON string representation of the object
print(ObjectImportResult1.to_json())

# convert the object into a dict
object_import_result1_dict = object_import_result1_instance.to_dict()
# create an instance of ObjectImportResult1 from a dict
object_import_result1_from_dict = ObjectImportResult1.from_dict(object_import_result1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


