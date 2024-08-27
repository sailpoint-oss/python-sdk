# AccessRequestRecommendationActionItemResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The identity ID taking the action. | [optional] 
**access** | [**AccessRequestRecommendationItem**](AccessRequestRecommendationItem.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationActionItemResponseDto from a JSON string
access_request_recommendation_action_item_response_dto_instance = AccessRequestRecommendationActionItemResponseDto.from_json(json)
# print the JSON string representation of the object
print(AccessRequestRecommendationActionItemResponseDto.to_json())

# convert the object into a dict
access_request_recommendation_action_item_response_dto_dict = access_request_recommendation_action_item_response_dto_instance.to_dict()
# create an instance of AccessRequestRecommendationActionItemResponseDto from a dict
access_request_recommendation_action_item_response_dto_from_dict = AccessRequestRecommendationActionItemResponseDto.from_dict(access_request_recommendation_action_item_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


