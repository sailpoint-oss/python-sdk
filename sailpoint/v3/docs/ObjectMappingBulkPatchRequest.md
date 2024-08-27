# ObjectMappingBulkPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patches** | **Dict[str, List[JsonPatchOperation]]** | Map of id of the object mapping to a JsonPatchOperation describing what to patch on that object mapping. | 

## Example

```python
from sailpoint.v3.models.object_mapping_bulk_patch_request import ObjectMappingBulkPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingBulkPatchRequest from a JSON string
object_mapping_bulk_patch_request_instance = ObjectMappingBulkPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectMappingBulkPatchRequest.to_json())

# convert the object into a dict
object_mapping_bulk_patch_request_dict = object_mapping_bulk_patch_request_instance.to_dict()
# create an instance of ObjectMappingBulkPatchRequest from a dict
object_mapping_bulk_patch_request_from_dict = ObjectMappingBulkPatchRequest.from_dict(object_mapping_bulk_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


