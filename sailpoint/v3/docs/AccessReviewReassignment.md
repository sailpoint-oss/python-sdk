# AccessReviewReassignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassign** | [**List[ReassignReference]**](ReassignReference.md) |  | 
**reassign_to** | **str** | The ID of the identity to which the certification is reassigned | 
**reason** | **str** | The reason comment for why the reassign was made | 

## Example

```python
from sailpoint.v3.models.access_review_reassignment import AccessReviewReassignment

# TODO update the JSON string below
json = "{}"
# create an instance of AccessReviewReassignment from a JSON string
access_review_reassignment_instance = AccessReviewReassignment.from_json(json)
# print the JSON string representation of the object
print(AccessReviewReassignment.to_json())

# convert the object into a dict
access_review_reassignment_dict = access_review_reassignment_instance.to_dict()
# create an instance of AccessReviewReassignment from a dict
access_review_reassignment_from_dict = AccessReviewReassignment.from_dict(access_review_reassignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


