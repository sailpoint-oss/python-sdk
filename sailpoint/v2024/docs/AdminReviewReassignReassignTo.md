# AdminReviewReassignReassignTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identity ID to which the review is being assigned. | [optional] 
**type** | **str** | The type of the ID provided. | [optional] 

## Example

```python
from sailpoint.v2024.models.admin_review_reassign_reassign_to import AdminReviewReassignReassignTo

# TODO update the JSON string below
json = "{}"
# create an instance of AdminReviewReassignReassignTo from a JSON string
admin_review_reassign_reassign_to_instance = AdminReviewReassignReassignTo.from_json(json)
# print the JSON string representation of the object
print(AdminReviewReassignReassignTo.to_json())

# convert the object into a dict
admin_review_reassign_reassign_to_dict = admin_review_reassign_reassign_to_instance.to_dict()
# create an instance of AdminReviewReassignReassignTo from a dict
admin_review_reassign_reassign_to_from_dict = AdminReviewReassignReassignTo.from_dict(admin_review_reassign_reassign_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


