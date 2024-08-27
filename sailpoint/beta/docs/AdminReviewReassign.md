# AdminReviewReassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification_ids** | **List[str]** | List of certification IDs to reassign | [optional] 
**reassign_to** | [**AdminReviewReassignReassignTo**](AdminReviewReassignReassignTo.md) |  | [optional] 
**reason** | **str** | Comment to explain why the certification was reassigned | [optional] 

## Example

```python
from sailpoint.beta.models.admin_review_reassign import AdminReviewReassign

# TODO update the JSON string below
json = "{}"
# create an instance of AdminReviewReassign from a JSON string
admin_review_reassign_instance = AdminReviewReassign.from_json(json)
# print the JSON string representation of the object
print(AdminReviewReassign.to_json())

# convert the object into a dict
admin_review_reassign_dict = admin_review_reassign_instance.to_dict()
# create an instance of AdminReviewReassign from a dict
admin_review_reassign_from_dict = AdminReviewReassign.from_dict(admin_review_reassign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


