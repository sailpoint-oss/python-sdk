# JsonPatchOperation

A JSONPatch Operation as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation to be performed | 
**path** | **str** | A string JSON Pointer representing the target path to an element to be affected by the operation | 
**value** | [**JsonPatchOperationValue**](JsonPatchOperationValue.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.json_patch_operation import JsonPatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchOperation from a JSON string
json_patch_operation_instance = JsonPatchOperation.from_json(json)
# print the JSON string representation of the object
print JsonPatchOperation.to_json()

# convert the object into a dict
json_patch_operation_dict = json_patch_operation_instance.to_dict()
# create an instance of JsonPatchOperation from a dict
json_patch_operation_form_dict = json_patch_operation.from_dict(json_patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


