# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commenter_id** | **str** | Id of the identity making the comment | [optional] 
**commenter_name** | **str** | Human-readable display name of the identity making the comment | [optional] 
**body** | **str** | Content of the comment | [optional] 
**var_date** | **datetime** | Date and time comment was made | [optional] 

## Example

```python
from sailpoint.v2024.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


