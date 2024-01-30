# FullcampaignAllOfSearchCampaignInfo

Must be set only if the campaign type is SEARCH.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of search campaign represented. | 
**description** | **str** | Describes this search campaign. Intended for storing the query used, and possibly the number of identities selected/available. | [optional] 
**reviewer** | [**FullcampaignAllOfSearchCampaignInfoReviewer**](FullcampaignAllOfSearchCampaignInfoReviewer.md) |  | [optional] 
**query** | **str** | The scope for the campaign. The campaign will cover identities returned by the query and identities that have access items returned by the query. One of &#x60;query&#x60; or &#x60;identityIds&#x60; must be set. | [optional] 
**identity_ids** | **List[str]** | A direct list of identities to include in this campaign. One of &#x60;identityIds&#x60; or &#x60;query&#x60; must be set. | [optional] 
**access_constraints** | [**List[AccessConstraint]**](AccessConstraint.md) | Further reduces the scope of the campaign by excluding identities (from &#x60;query&#x60; or &#x60;identityIds&#x60;) that do not have this access. | [optional] 

## Example

```python
from sailpoint.beta.models.fullcampaign_all_of_search_campaign_info import FullcampaignAllOfSearchCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfSearchCampaignInfo from a JSON string
fullcampaign_all_of_search_campaign_info_instance = FullcampaignAllOfSearchCampaignInfo.from_json(json)
# print the JSON string representation of the object
print FullcampaignAllOfSearchCampaignInfo.to_json()

# convert the object into a dict
fullcampaign_all_of_search_campaign_info_dict = fullcampaign_all_of_search_campaign_info_instance.to_dict()
# create an instance of FullcampaignAllOfSearchCampaignInfo from a dict
fullcampaign_all_of_search_campaign_info_form_dict = fullcampaign_all_of_search_campaign_info.from_dict(fullcampaign_all_of_search_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


