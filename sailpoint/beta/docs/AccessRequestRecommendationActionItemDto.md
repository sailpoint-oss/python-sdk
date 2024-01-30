# AccessRequestRecommendationActionItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID taking the action. | 
**access** | [**AccessRequestRecommendationItem**](AccessRequestRecommendationItem.md) |  | 

## Example

```python
from sailpoint.beta.models.access_request_recommendation_action_item_dto import AccessRequestRecommendationActionItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationActionItemDto from a JSON string
access_request_recommendation_action_item_dto_instance = AccessRequestRecommendationActionItemDto.from_json(json)
# print the JSON string representation of the object
print AccessRequestRecommendationActionItemDto.to_json()

# convert the object into a dict
access_request_recommendation_action_item_dto_dict = access_request_recommendation_action_item_dto_instance.to_dict()
# create an instance of AccessRequestRecommendationActionItemDto from a dict
access_request_recommendation_action_item_dto_form_dict = access_request_recommendation_action_item_dto.from_dict(access_request_recommendation_action_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


