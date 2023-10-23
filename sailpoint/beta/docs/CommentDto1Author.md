# CommentDto1Author


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**id** | **str** | ID of the author | [optional] 
**name** | **str** | Human-readable display name of the identity making the comment | [optional] 

## Example

```python
from beta.models.comment_dto1_author import CommentDto1Author

# TODO update the JSON string below
json = "{}"
# create an instance of CommentDto1Author from a JSON string
comment_dto1_author_instance = CommentDto1Author.from_json(json)
# print the JSON string representation of the object
print CommentDto1Author.to_json()

# convert the object into a dict
comment_dto1_author_dict = comment_dto1_author_instance.to_dict()
# create an instance of CommentDto1Author from a dict
comment_dto1_author_form_dict = comment_dto1_author.from_dict(comment_dto1_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


