# ListCampaignFilters200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CampaignFilterDetails]**](CampaignFilterDetails.md) | List of campaign filters. | [optional] 
**count** | **int** | Number of filters returned. | [optional] 

## Example

```python
from sailpoint.v3.models.list_campaign_filters200_response import ListCampaignFilters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCampaignFilters200Response from a JSON string
list_campaign_filters200_response_instance = ListCampaignFilters200Response.from_json(json)
# print the JSON string representation of the object
print(ListCampaignFilters200Response.to_json())

# convert the object into a dict
list_campaign_filters200_response_dict = list_campaign_filters200_response_instance.to_dict()
# create an instance of ListCampaignFilters200Response from a dict
list_campaign_filters200_response_from_dict = ListCampaignFilters200Response.from_dict(list_campaign_filters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


