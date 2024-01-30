# ReviewReassign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reassign** | [**List[ReassignReference]**](ReassignReference.md) |  | 
**reassign_to** | **str** | The ID of the identity to which the certification is reassigned | 
**reason** | **str** | The reason comment for why the reassign was made | 

## Example

```python
from sailpoint.beta.models.review_reassign import ReviewReassign

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewReassign from a JSON string
review_reassign_instance = ReviewReassign.from_json(json)
# print the JSON string representation of the object
print ReviewReassign.to_json()

# convert the object into a dict
review_reassign_dict = review_reassign_instance.to_dict()
# create an instance of ReviewReassign from a dict
review_reassign_form_dict = review_reassign.from_dict(review_reassign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


