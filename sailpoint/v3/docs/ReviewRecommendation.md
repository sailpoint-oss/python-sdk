# ReviewRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation** | **str** | The recommendation from IAI at the time of the decision. This field will be null if no recommendation was made. | [optional] 
**reasons** | **List[str]** | A list of reasons for the recommendation. | [optional] 
**timestamp** | **datetime** | The time at which the recommendation was recorded. | [optional] 

## Example

```python
from sailpoint.v3.models.review_recommendation import ReviewRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewRecommendation from a JSON string
review_recommendation_instance = ReviewRecommendation.from_json(json)
# print the JSON string representation of the object
print ReviewRecommendation.to_json()

# convert the object into a dict
review_recommendation_dict = review_recommendation_instance.to_dict()
# create an instance of ReviewRecommendation from a dict
review_recommendation_form_dict = review_recommendation.from_dict(review_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


