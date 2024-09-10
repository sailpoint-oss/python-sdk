# JsonPatchOperations

A limited JSONPatch Operation as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation to be performed | 
**path** | **str** | A string representing the target path to an element to be affected by the operation | 
**value** | [**JsonPatchOperationsValue**](JsonPatchOperationsValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.json_patch_operations import JsonPatchOperations

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchOperations from a JSON string
json_patch_operations_instance = JsonPatchOperations.from_json(json)
# print the JSON string representation of the object
print(JsonPatchOperations.to_json())

# convert the object into a dict
json_patch_operations_dict = json_patch_operations_instance.to_dict()
# create an instance of JsonPatchOperations from a dict
json_patch_operations_from_dict = JsonPatchOperations.from_dict(json_patch_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


