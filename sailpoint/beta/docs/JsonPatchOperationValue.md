# JsonPatchOperationValue

The value to be used for the operation, required for \"add\" and \"replace\" operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.beta.models.json_patch_operation_value import JsonPatchOperationValue

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchOperationValue from a JSON string
json_patch_operation_value_instance = JsonPatchOperationValue.from_json(json)
# print the JSON string representation of the object
print JsonPatchOperationValue.to_json()

# convert the object into a dict
json_patch_operation_value_dict = json_patch_operation_value_instance.to_dict()
# create an instance of JsonPatchOperationValue from a dict
json_patch_operation_value_form_dict = json_patch_operation_value.from_dict(json_patch_operation_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


