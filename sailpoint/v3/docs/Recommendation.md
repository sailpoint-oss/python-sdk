# Recommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Recommended type of account. | 
**method** | **str** | Method used to produce the recommendation. DISCOVERY - suggested by AI, SOURCE - the account comes from a source flagged as containing machine accounts, CRITERIA - the account satisfies classification criteria. | 

## Example

```python
from sailpoint.v3.models.recommendation import Recommendation

# TODO update the JSON string below
json = "{}"
# create an instance of Recommendation from a JSON string
recommendation_instance = Recommendation.from_json(json)
# print the JSON string representation of the object
print(Recommendation.to_json())

# convert the object into a dict
recommendation_dict = recommendation_instance.to_dict()
# create an instance of Recommendation from a dict
recommendation_from_dict = Recommendation.from_dict(recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


