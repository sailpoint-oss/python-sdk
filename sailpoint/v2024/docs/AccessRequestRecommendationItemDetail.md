# AccessRequestRecommendationItemDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | Identity ID for the recommendation | [optional] 
**access** | [**AccessRequestRecommendationItemDetailAccess**](AccessRequestRecommendationItemDetailAccess.md) |  | [optional] 
**ignored** | **bool** | Whether or not the identity has already chosen to ignore this recommendation. | [optional] 
**requested** | **bool** | Whether or not the identity has already chosen to request this recommendation. | [optional] 
**viewed** | **bool** | Whether or not the identity reportedly viewed this recommendation. | [optional] 
**messages** | [**List[AccessRecommendationMessage]**](AccessRecommendationMessage.md) |  | [optional] 
**translation_messages** | [**List[TranslationMessage]**](TranslationMessage.md) | The list of translation messages | [optional] 

## Example

```python
from sailpoint.v2024.models.access_request_recommendation_item_detail import AccessRequestRecommendationItemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationItemDetail from a JSON string
access_request_recommendation_item_detail_instance = AccessRequestRecommendationItemDetail.from_json(json)
# print the JSON string representation of the object
print AccessRequestRecommendationItemDetail.to_json()

# convert the object into a dict
access_request_recommendation_item_detail_dict = access_request_recommendation_item_detail_instance.to_dict()
# create an instance of AccessRequestRecommendationItemDetail from a dict
access_request_recommendation_item_detail_form_dict = access_request_recommendation_item_detail.from_dict(access_request_recommendation_item_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


