# RecommendationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[RecommendationRequest]**](RecommendationRequest.md) |  | [optional] 
**exclude_interpretations** | **bool** | Exclude interpretations in the response if \&quot;true\&quot;. Return interpretations in the response if this attribute is not specified. | [optional] [default to False]
**include_translation_messages** | **bool** | When set to true, the calling system uses the translated messages for the specified language | [optional] [default to False]
**include_debug_information** | **bool** | Returns the recommender calculations if set to true | [optional] [default to False]
**prescribe_mode** | **bool** | When set to true, uses prescribedRulesRecommenderConfig to get identity attributes and peer group threshold instead of standard config. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.recommendation_request_dto import RecommendationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationRequestDto from a JSON string
recommendation_request_dto_instance = RecommendationRequestDto.from_json(json)
# print the JSON string representation of the object
print(RecommendationRequestDto.to_json())

# convert the object into a dict
recommendation_request_dto_dict = recommendation_request_dto_instance.to_dict()
# create an instance of RecommendationRequestDto from a dict
recommendation_request_dto_from_dict = RecommendationRequestDto.from_dict(recommendation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


