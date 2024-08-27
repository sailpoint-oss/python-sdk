# AccessRequestRecommendationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of access item being recommended. | [optional] 
**type** | [**AccessRequestRecommendationItemType**](AccessRequestRecommendationItemType.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.access_request_recommendation_item import AccessRequestRecommendationItem

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationItem from a JSON string
access_request_recommendation_item_instance = AccessRequestRecommendationItem.from_json(json)
# print the JSON string representation of the object
print(AccessRequestRecommendationItem.to_json())

# convert the object into a dict
access_request_recommendation_item_dict = access_request_recommendation_item_instance.to_dict()
# create an instance of AccessRequestRecommendationItem from a dict
access_request_recommendation_item_from_dict = AccessRequestRecommendationItem.from_dict(access_request_recommendation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


