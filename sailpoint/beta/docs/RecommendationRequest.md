# RecommendationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID | [optional] 
**item** | [**AccessItemRef**](AccessItemRef.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.recommendation_request import RecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationRequest from a JSON string
recommendation_request_instance = RecommendationRequest.from_json(json)
# print the JSON string representation of the object
print RecommendationRequest.to_json()

# convert the object into a dict
recommendation_request_dict = recommendation_request_instance.to_dict()
# create an instance of RecommendationRequest from a dict
recommendation_request_form_dict = recommendation_request.from_dict(recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


