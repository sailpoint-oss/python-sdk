# ReviewDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the review decision | 
**decision** | [**CertificationDecision**](CertificationDecision.md) |  | 
**proposed_end_date** | **datetime** | The date at which a user&#39;s access should be taken away. Should only be set for &#x60;REVOKE&#x60; decisions. | [optional] 
**bulk** | **bool** | Indicates whether decision should be marked as part of a larger bulk decision | 
**recommendation** | [**ReviewRecommendation**](ReviewRecommendation.md) |  | [optional] 
**comments** | **str** | Comments recorded when the decision was made | [optional] 

## Example

```python
from sailpoint.v3.models.review_decision import ReviewDecision

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewDecision from a JSON string
review_decision_instance = ReviewDecision.from_json(json)
# print the JSON string representation of the object
print ReviewDecision.to_json()

# convert the object into a dict
review_decision_dict = review_decision_instance.to_dict()
# create an instance of ReviewDecision from a dict
review_decision_form_dict = review_decision.from_dict(review_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


