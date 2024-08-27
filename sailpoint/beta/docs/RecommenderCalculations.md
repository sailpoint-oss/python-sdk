# RecommenderCalculations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The ID of the identity | [optional] 
**entitlement_id** | **str** | The entitlement ID | [optional] 
**recommendation** | **str** | The actual recommendation | [optional] 
**overall_weighted_score** | **float** | The overall weighted score | [optional] 
**feature_weighted_scores** | **Dict[str, float]** | The weighted score of each individual feature | [optional] 
**threshold** | **float** | The configured value against which the overallWeightedScore is compared | [optional] 
**identity_attributes** | [**Dict[str, RecommenderCalculationsIdentityAttributesValue]**](RecommenderCalculationsIdentityAttributesValue.md) | The values for your configured features | [optional] 
**feature_values** | [**FeatureValueDto**](FeatureValueDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.recommender_calculations import RecommenderCalculations

# TODO update the JSON string below
json = "{}"
# create an instance of RecommenderCalculations from a JSON string
recommender_calculations_instance = RecommenderCalculations.from_json(json)
# print the JSON string representation of the object
print(RecommenderCalculations.to_json())

# convert the object into a dict
recommender_calculations_dict = recommender_calculations_instance.to_dict()
# create an instance of RecommenderCalculations from a dict
recommender_calculations_from_dict = RecommenderCalculations.from_dict(recommender_calculations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


