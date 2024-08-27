# BulkTaggedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_refs** | [**List[TaggedObjectDto]**](TaggedObjectDto.md) |  | [optional] 
**tags** | **List[str]** | Label to be applied to object. | [optional] 
**operation** | **str** | If APPEND, tags are appended to the list of tags for the object. A 400 error is returned if this would add duplicate tags to the object.  If MERGE, tags are merged with the existing tags. Duplicate tags are silently ignored. | [optional] [default to 'APPEND']

## Example

```python
from sailpoint.beta.models.bulk_tagged_object import BulkTaggedObject

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTaggedObject from a JSON string
bulk_tagged_object_instance = BulkTaggedObject.from_json(json)
# print the JSON string representation of the object
print(BulkTaggedObject.to_json())

# convert the object into a dict
bulk_tagged_object_dict = bulk_tagged_object_instance.to_dict()
# create an instance of BulkTaggedObject from a dict
bulk_tagged_object_from_dict = BulkTaggedObject.from_dict(bulk_tagged_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


