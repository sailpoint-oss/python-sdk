# CompletedApprovalReviewerComment

The approval's reviewer's comment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment content. | [optional] 
**author** | [**CommentDtoAuthor**](CommentDtoAuthor.md) |  | [optional] 
**created** | **datetime** | Date and time comment was created. | [optional] 

## Example

```python
from v3.models.completed_approval_reviewer_comment import CompletedApprovalReviewerComment

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedApprovalReviewerComment from a JSON string
completed_approval_reviewer_comment_instance = CompletedApprovalReviewerComment.from_json(json)
# print the JSON string representation of the object
print CompletedApprovalReviewerComment.to_json()

# convert the object into a dict
completed_approval_reviewer_comment_dict = completed_approval_reviewer_comment_instance.to_dict()
# create an instance of CompletedApprovalReviewerComment from a dict
completed_approval_reviewer_comment_form_dict = completed_approval_reviewer_comment.from_dict(completed_approval_reviewer_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


