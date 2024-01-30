# CompletedApprovalReviewedBy

Identity who reviewed the access item request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | DTO type of identity who reviewed the access item request. | [optional] 
**id** | **str** | ID of identity who reviewed the access item request. | [optional] 
**name** | **str** | Human-readable display name of identity who reviewed the access item request. | [optional] 

## Example

```python
from sailpoint.beta.models.completed_approval_reviewed_by import CompletedApprovalReviewedBy

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedApprovalReviewedBy from a JSON string
completed_approval_reviewed_by_instance = CompletedApprovalReviewedBy.from_json(json)
# print the JSON string representation of the object
print CompletedApprovalReviewedBy.to_json()

# convert the object into a dict
completed_approval_reviewed_by_dict = completed_approval_reviewed_by_instance.to_dict()
# create an instance of CompletedApprovalReviewedBy from a dict
completed_approval_reviewed_by_form_dict = completed_approval_reviewed_by.from_dict(completed_approval_reviewed_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


