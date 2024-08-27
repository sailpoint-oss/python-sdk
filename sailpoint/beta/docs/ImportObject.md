# ImportObject

Object created or updated by import.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of object created or updated by import. | [optional] 
**id** | **str** | ID of object created or updated by import. | [optional] 
**name** | **str** | Display name of object created or updated by import. | [optional] 

## Example

```python
from sailpoint.beta.models.import_object import ImportObject

# TODO update the JSON string below
json = "{}"
# create an instance of ImportObject from a JSON string
import_object_instance = ImportObject.from_json(json)
# print the JSON string representation of the object
print(ImportObject.to_json())

# convert the object into a dict
import_object_dict = import_object_instance.to_dict()
# create an instance of ImportObject from a dict
import_object_from_dict = ImportObject.from_dict(import_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


