# CompletedApprovalRequesterComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment content. | [optional] 
**created** | **datetime** | Date and time comment was created. | [optional] 
**author** | [**CommentDtoAuthor**](CommentDtoAuthor.md) |  | [optional] 

## Example

```python
from sailpoint.v3.models.completed_approval_requester_comment import CompletedApprovalRequesterComment

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedApprovalRequesterComment from a JSON string
completed_approval_requester_comment_instance = CompletedApprovalRequesterComment.from_json(json)
# print the JSON string representation of the object
print(CompletedApprovalRequesterComment.to_json())

# convert the object into a dict
completed_approval_requester_comment_dict = completed_approval_requester_comment_instance.to_dict()
# create an instance of CompletedApprovalRequesterComment from a dict
completed_approval_requester_comment_from_dict = CompletedApprovalRequesterComment.from_dict(completed_approval_requester_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


