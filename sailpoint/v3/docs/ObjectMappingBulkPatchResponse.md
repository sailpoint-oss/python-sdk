# ObjectMappingBulkPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patched_objects** | [**List[ObjectMappingResponse]**](ObjectMappingResponse.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.object_mapping_bulk_patch_response import ObjectMappingBulkPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingBulkPatchResponse from a JSON string
object_mapping_bulk_patch_response_instance = ObjectMappingBulkPatchResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectMappingBulkPatchResponse.to_json())

# convert the object into a dict
object_mapping_bulk_patch_response_dict = object_mapping_bulk_patch_response_instance.to_dict()
# create an instance of ObjectMappingBulkPatchResponse from a dict
object_mapping_bulk_patch_response_from_dict = ObjectMappingBulkPatchResponse.from_dict(object_mapping_bulk_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


