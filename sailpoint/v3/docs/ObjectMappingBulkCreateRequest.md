# ObjectMappingBulkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_object_mappings** | [**List[ObjectMappingRequest]**](ObjectMappingRequest.md) |  | 

## Example

```python
from sailpoint.v3.models.object_mapping_bulk_create_request import ObjectMappingBulkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingBulkCreateRequest from a JSON string
object_mapping_bulk_create_request_instance = ObjectMappingBulkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectMappingBulkCreateRequest.to_json())

# convert the object into a dict
object_mapping_bulk_create_request_dict = object_mapping_bulk_create_request_instance.to_dict()
# create an instance of ObjectMappingBulkCreateRequest from a dict
object_mapping_bulk_create_request_from_dict = ObjectMappingBulkCreateRequest.from_dict(object_mapping_bulk_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


