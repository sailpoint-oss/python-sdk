# CommentDtoAuthor

Author of the comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of object | [optional] 
**id** | **str** | The unique ID of the object | [optional] 
**name** | **str** | The display name of the object | [optional] 

## Example

```python
from sailpoint.v2024.models.comment_dto_author import CommentDtoAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of CommentDtoAuthor from a JSON string
comment_dto_author_instance = CommentDtoAuthor.from_json(json)
# print the JSON string representation of the object
print(CommentDtoAuthor.to_json())

# convert the object into a dict
comment_dto_author_dict = comment_dto_author_instance.to_dict()
# create an instance of CommentDtoAuthor from a dict
comment_dto_author_from_dict = CommentDtoAuthor.from_dict(comment_dto_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


