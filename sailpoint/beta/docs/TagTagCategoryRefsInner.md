# TagTagCategoryRefsInner

Tagged object's category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of the tagged object&#39;s category. | [optional] 
**id** | **str** | Tagged object&#39;s ID. | [optional] 
**name** | **str** | Tagged object&#39;s display name. | [optional] 

## Example

```python
from sailpoint.beta.models.tag_tag_category_refs_inner import TagTagCategoryRefsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TagTagCategoryRefsInner from a JSON string
tag_tag_category_refs_inner_instance = TagTagCategoryRefsInner.from_json(json)
# print the JSON string representation of the object
print(TagTagCategoryRefsInner.to_json())

# convert the object into a dict
tag_tag_category_refs_inner_dict = tag_tag_category_refs_inner_instance.to_dict()
# create an instance of TagTagCategoryRefsInner from a dict
tag_tag_category_refs_inner_from_dict = TagTagCategoryRefsInner.from_dict(tag_tag_category_refs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


