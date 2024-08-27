# RecommendationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**RecommendationRequest**](RecommendationRequest.md) |  | [optional] 
**recommendation** | **str** | The recommendation - YES if the access is recommended, NO if not recommended, MAYBE if there is not enough information to make a recommendation, NOT_FOUND if the identity is not found in the system | [optional] 
**interpretations** | **List[str]** | The list of interpretations explaining the recommendation. The array is empty if includeInterpretations is false or not present in the request. e.g. - [ \&quot;Not approved in the last 6 months.\&quot; ]. Interpretations will be translated using the client&#39;s locale as found in the Accept-Language header. If a translation for the client&#39;s locale cannot be found, the US English translation will be returned. | [optional] 
**translation_messages** | [**List[TranslationMessage]**](TranslationMessage.md) | The list of translation messages, if they have been requested. | [optional] 
**recommender_calculations** | [**RecommenderCalculations**](RecommenderCalculations.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.recommendation_response import RecommendationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationResponse from a JSON string
recommendation_response_instance = RecommendationResponse.from_json(json)
# print the JSON string representation of the object
print(RecommendationResponse.to_json())

# convert the object into a dict
recommendation_response_dict = recommendation_response_instance.to_dict()
# create an instance of RecommendationResponse from a dict
recommendation_response_from_dict = RecommendationResponse.from_dict(recommendation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


