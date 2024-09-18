# ApprovalComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment provided either by the approval requester or the approver. | 
**timestamp** | **datetime** | The time when this comment was provided. | 
**user** | **str** | Name of the user that provided this comment. | 
**id** | **str** | Id of the user that provided this comment. | 
**changed_to_status** | **str** | Status transition of the draft. | 

## Example

```python
from sailpoint.v2024.models.approval_comment import ApprovalComment

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalComment from a JSON string
approval_comment_instance = ApprovalComment.from_json(json)
# print the JSON string representation of the object
print(ApprovalComment.to_json())

# convert the object into a dict
approval_comment_dict = approval_comment_instance.to_dict()
# create an instance of ApprovalComment from a dict
approval_comment_from_dict = ApprovalComment.from_dict(approval_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


