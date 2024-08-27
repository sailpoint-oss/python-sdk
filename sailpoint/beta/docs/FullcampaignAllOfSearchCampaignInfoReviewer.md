# FullcampaignAllOfSearchCampaignInfoReviewer

If specified, this identity or governance group will be the reviewer for all certifications in this campaign. The allowed DTO types are IDENTITY and GOVERNANCE_GROUP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The reviewer&#39;s DTO type. | [optional] 
**id** | **str** | The reviewer&#39;s ID. | [optional] 
**name** | **str** | The reviewer&#39;s name. | [optional] 

## Example

```python
from sailpoint.beta.models.fullcampaign_all_of_search_campaign_info_reviewer import FullcampaignAllOfSearchCampaignInfoReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfSearchCampaignInfoReviewer from a JSON string
fullcampaign_all_of_search_campaign_info_reviewer_instance = FullcampaignAllOfSearchCampaignInfoReviewer.from_json(json)
# print the JSON string representation of the object
print(FullcampaignAllOfSearchCampaignInfoReviewer.to_json())

# convert the object into a dict
fullcampaign_all_of_search_campaign_info_reviewer_dict = fullcampaign_all_of_search_campaign_info_reviewer_instance.to_dict()
# create an instance of FullcampaignAllOfSearchCampaignInfoReviewer from a dict
fullcampaign_all_of_search_campaign_info_reviewer_from_dict = FullcampaignAllOfSearchCampaignInfoReviewer.from_dict(fullcampaign_all_of_search_campaign_info_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


