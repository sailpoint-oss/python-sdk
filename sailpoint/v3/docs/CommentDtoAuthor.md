# CommentDtoAuthor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of the commenting identity. | [optional] 
**id** | **str** | ID of the commenting identity. | [optional] 
**name** | **str** | Display name of the commenting identity. | [optional] 

## Example

```python
from sailpoint.v3.models.comment_dto_author import CommentDtoAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of CommentDtoAuthor from a JSON string
comment_dto_author_instance = CommentDtoAuthor.from_json(json)
# print the JSON string representation of the object
print CommentDtoAuthor.to_json()

# convert the object into a dict
comment_dto_author_dict = comment_dto_author_instance.to_dict()
# create an instance of CommentDtoAuthor from a dict
comment_dto_author_form_dict = comment_dto_author.from_dict(comment_dto_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


