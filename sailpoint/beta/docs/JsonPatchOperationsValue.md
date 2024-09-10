# JsonPatchOperationsValue

The value to be used for the operation, required for \"add\" and \"replace\" operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.beta.models.json_patch_operations_value import JsonPatchOperationsValue

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchOperationsValue from a JSON string
json_patch_operations_value_instance = JsonPatchOperationsValue.from_json(json)
# print the JSON string representation of the object
print(JsonPatchOperationsValue.to_json())

# convert the object into a dict
json_patch_operations_value_dict = json_patch_operations_value_instance.to_dict()
# create an instance of JsonPatchOperationsValue from a dict
json_patch_operations_value_from_dict = JsonPatchOperationsValue.from_dict(json_patch_operations_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


