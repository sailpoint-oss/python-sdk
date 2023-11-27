# AccessRequestRecommendationItemDetailAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of access item being recommended. | [optional] 
**type** | [**AccessRequestRecommendationItemType**](AccessRequestRecommendationItemType.md) |  | [optional] 
**name** | **str** | Name of the access item | [optional] 
**description** | **str** | Description of the access item | [optional] 

## Example

```python
from sailpoint.beta.models.access_request_recommendation_item_detail_access import AccessRequestRecommendationItemDetailAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationItemDetailAccess from a JSON string
access_request_recommendation_item_detail_access_instance = AccessRequestRecommendationItemDetailAccess.from_json(json)
# print the JSON string representation of the object
print AccessRequestRecommendationItemDetailAccess.to_json()

# convert the object into a dict
access_request_recommendation_item_detail_access_dict = access_request_recommendation_item_detail_access_instance.to_dict()
# create an instance of AccessRequestRecommendationItemDetailAccess from a dict
access_request_recommendation_item_detail_access_form_dict = access_request_recommendation_item_detail_access.from_dict(access_request_recommendation_item_detail_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


