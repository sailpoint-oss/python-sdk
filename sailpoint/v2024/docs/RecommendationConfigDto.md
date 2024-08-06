# RecommendationConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommender_features** | **List[str]** | List of identity attributes to use for calculating certification recommendations | [optional] 
**peer_group_percentage_threshold** | **float** | The percent value that the recommendation calculation must surpass to produce a YES recommendation | [optional] 
**run_auto_select_once** | **bool** | If true, rulesRecommenderConfig will be refreshed with new programatically selected attribute and threshold values on the next pipeline run | [optional] [default to False]
**only_tune_threshold** | **bool** | If true, rulesRecommenderConfig will be refreshed with new programatically selected threshold values on the next pipeline run | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.recommendation_config_dto import RecommendationConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationConfigDto from a JSON string
recommendation_config_dto_instance = RecommendationConfigDto.from_json(json)
# print the JSON string representation of the object
print RecommendationConfigDto.to_json()

# convert the object into a dict
recommendation_config_dto_dict = recommendation_config_dto_instance.to_dict()
# create an instance of RecommendationConfigDto from a dict
recommendation_config_dto_form_dict = recommendation_config_dto.from_dict(recommendation_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


