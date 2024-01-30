# ApprovalComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | The comment text | [optional] 
**commenter** | **str** | The name of the commenter | [optional] 
**var_date** | **datetime** | A date-time in ISO-8601 format | [optional] 

## Example

```python
from sailpoint.v3.models.approval_comment import ApprovalComment

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalComment from a JSON string
approval_comment_instance = ApprovalComment.from_json(json)
# print the JSON string representation of the object
print ApprovalComment.to_json()

# convert the object into a dict
approval_comment_dict = approval_comment_instance.to_dict()
# create an instance of ApprovalComment from a dict
approval_comment_form_dict = approval_comment.from_dict(approval_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


