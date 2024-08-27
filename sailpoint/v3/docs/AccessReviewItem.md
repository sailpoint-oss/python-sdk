# AccessReviewItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_summary** | [**AccessSummary**](AccessSummary.md) |  | [optional] 
**identity_summary** | [**CertificationIdentitySummary**](CertificationIdentitySummary.md) |  | [optional] 
**id** | **str** | The review item&#39;s id | [optional] 
**completed** | **bool** | Whether the review item is complete | [optional] 
**new_access** | **bool** | Indicates whether the review item is for new access to a source | [optional] 
**decision** | [**CertificationDecision**](CertificationDecision.md) |  | [optional] 
**comments** | **str** | Comments for this review item | [optional] 

## Example

```python
from sailpoint.v3.models.access_review_item import AccessReviewItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessReviewItem from a JSON string
access_review_item_instance = AccessReviewItem.from_json(json)
# print the JSON string representation of the object
print(AccessReviewItem.to_json())

# convert the object into a dict
access_review_item_dict = access_review_item_instance.to_dict()
# create an instance of AccessReviewItem from a dict
access_review_item_from_dict = AccessReviewItem.from_dict(access_review_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


