# BulkTaggedObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_refs** | [**List[TaggedObjectDto]**](TaggedObjectDto.md) |  | [optional] 
**tags** | **List[str]** | Label to be applied to an Object | [optional] 

## Example

```python
from sailpoint.v2024.models.bulk_tagged_object_response import BulkTaggedObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTaggedObjectResponse from a JSON string
bulk_tagged_object_response_instance = BulkTaggedObjectResponse.from_json(json)
# print the JSON string representation of the object
print(BulkTaggedObjectResponse.to_json())

# convert the object into a dict
bulk_tagged_object_response_dict = bulk_tagged_object_response_instance.to_dict()
# create an instance of BulkTaggedObjectResponse from a dict
bulk_tagged_object_response_from_dict = BulkTaggedObjectResponse.from_dict(bulk_tagged_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


