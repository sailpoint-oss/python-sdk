# BulkAddTaggedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_refs** | [**List[TaggedObjectDto]**](TaggedObjectDto.md) |  | [optional] 
**tags** | **List[str]** | Label to be applied to an Object | [optional] 
**operation** | **str** | If APPEND, tags are appended to the list of tags for the object. A 400 error is returned if this would add duplicate tags to the object.  If MERGE, tags are merged with the existing tags. Duplicate tags are silently ignored. | [optional] [default to 'APPEND']

## Example

```python
from sailpoint.v3.models.bulk_add_tagged_object import BulkAddTaggedObject

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAddTaggedObject from a JSON string
bulk_add_tagged_object_instance = BulkAddTaggedObject.from_json(json)
# print the JSON string representation of the object
print BulkAddTaggedObject.to_json()

# convert the object into a dict
bulk_add_tagged_object_dict = bulk_add_tagged_object_instance.to_dict()
# create an instance of BulkAddTaggedObject from a dict
bulk_add_tagged_object_form_dict = bulk_add_tagged_object.from_dict(bulk_add_tagged_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


