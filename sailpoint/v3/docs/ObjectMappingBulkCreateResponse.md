# ObjectMappingBulkCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_objects** | [**List[ObjectMappingResponse]**](ObjectMappingResponse.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.object_mapping_bulk_create_response import ObjectMappingBulkCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMappingBulkCreateResponse from a JSON string
object_mapping_bulk_create_response_instance = ObjectMappingBulkCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ObjectMappingBulkCreateResponse.to_json())

# convert the object into a dict
object_mapping_bulk_create_response_dict = object_mapping_bulk_create_response_instance.to_dict()
# create an instance of ObjectMappingBulkCreateResponse from a dict
object_mapping_bulk_create_response_from_dict = ObjectMappingBulkCreateResponse.from_dict(object_mapping_bulk_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


