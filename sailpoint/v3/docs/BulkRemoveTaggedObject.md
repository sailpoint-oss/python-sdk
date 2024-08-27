# BulkRemoveTaggedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_refs** | [**List[TaggedObjectDto]**](TaggedObjectDto.md) |  | [optional] 
**tags** | **List[str]** | Label to be applied to an Object | [optional] 

## Example

```python
from sailpoint.v3.models.bulk_remove_tagged_object import BulkRemoveTaggedObject

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRemoveTaggedObject from a JSON string
bulk_remove_tagged_object_instance = BulkRemoveTaggedObject.from_json(json)
# print the JSON string representation of the object
print(BulkRemoveTaggedObject.to_json())

# convert the object into a dict
bulk_remove_tagged_object_dict = bulk_remove_tagged_object_instance.to_dict()
# create an instance of BulkRemoveTaggedObject from a dict
bulk_remove_tagged_object_from_dict = BulkRemoveTaggedObject.from_dict(bulk_remove_tagged_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


