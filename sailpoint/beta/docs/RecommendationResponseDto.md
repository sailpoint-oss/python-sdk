# RecommendationResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[RecommendationResponse]**](RecommendationResponse.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.recommendation_response_dto import RecommendationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationResponseDto from a JSON string
recommendation_response_dto_instance = RecommendationResponseDto.from_json(json)
# print the JSON string representation of the object
print RecommendationResponseDto.to_json()

# convert the object into a dict
recommendation_response_dto_dict = recommendation_response_dto_instance.to_dict()
# create an instance of RecommendationResponseDto from a dict
recommendation_response_dto_form_dict = recommendation_response_dto.from_dict(recommendation_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


