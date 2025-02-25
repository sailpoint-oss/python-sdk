# AccessRequestRecommendationConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score_threshold** | **float** | The value that internal calculations need to exceed for recommendations to be made. | 
**start_date_attribute** | **str** | Use to map an attribute name for determining identities&#39; start date. | [optional] 
**restriction_attribute** | **str** | Use to only give recommendations based on this attribute. | [optional] 
**mover_attribute** | **str** | Use to map an attribute name for determining whether identities are movers. | [optional] 
**joiner_attribute** | **str** | Use to map an attribute name for determining whether identities are joiners. | [optional] 
**use_restriction_attribute** | **bool** | Use only the attribute named in restrictionAttribute to make recommendations. | [optional] [default to False]

## Example

```python
from sailpoint.v2024.models.access_request_recommendation_config_dto import AccessRequestRecommendationConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestRecommendationConfigDto from a JSON string
access_request_recommendation_config_dto_instance = AccessRequestRecommendationConfigDto.from_json(json)
# print the JSON string representation of the object
print(AccessRequestRecommendationConfigDto.to_json())

# convert the object into a dict
access_request_recommendation_config_dto_dict = access_request_recommendation_config_dto_instance.to_dict()
# create an instance of AccessRequestRecommendationConfigDto from a dict
access_request_recommendation_config_dto_from_dict = AccessRequestRecommendationConfigDto.from_dict(access_request_recommendation_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


