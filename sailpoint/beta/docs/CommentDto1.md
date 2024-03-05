# CommentDto1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment content. | [optional] 
**created** | **datetime** | Date and time comment was created. | [optional] 
**author** | [**CommentDto1Author**](CommentDto1Author.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.comment_dto1 import CommentDto1

# TODO update the JSON string below
json = "{}"
# create an instance of CommentDto1 from a JSON string
comment_dto1_instance = CommentDto1.from_json(json)
# print the JSON string representation of the object
print CommentDto1.to_json()

# convert the object into a dict
comment_dto1_dict = comment_dto1_instance.to_dict()
# create an instance of CommentDto1 from a dict
comment_dto1_form_dict = comment_dto1.from_dict(comment_dto1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


