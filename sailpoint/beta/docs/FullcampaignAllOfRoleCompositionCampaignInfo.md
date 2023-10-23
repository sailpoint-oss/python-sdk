# FullcampaignAllOfRoleCompositionCampaignInfo

Optional configuration options for role composition campaigns.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer** | [**FullcampaignAllOfSearchCampaignInfoReviewer**](FullcampaignAllOfSearchCampaignInfoReviewer.md) |  | [optional] 
**role_ids** | **List[str]** | Optional list of roles to include in this campaign. Only one of &#x60;roleIds&#x60; and &#x60;query&#x60; may be set; if neither are set, all roles are included. | [optional] 
**remediator_ref** | [**FullcampaignAllOfRoleCompositionCampaignInfoRemediatorRef**](FullcampaignAllOfRoleCompositionCampaignInfoRemediatorRef.md) |  | 
**query** | **str** | Optional search query to scope this campaign to a set of roles. Only one of &#x60;roleIds&#x60; and &#x60;query&#x60; may be set; if neither are set, all roles are included. | [optional] 
**description** | **str** | Describes this role composition campaign. Intended for storing the query used, and possibly the number of roles selected/available. | [optional] 

## Example

```python
from beta.models.fullcampaign_all_of_role_composition_campaign_info import FullcampaignAllOfRoleCompositionCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfRoleCompositionCampaignInfo from a JSON string
fullcampaign_all_of_role_composition_campaign_info_instance = FullcampaignAllOfRoleCompositionCampaignInfo.from_json(json)
# print the JSON string representation of the object
print FullcampaignAllOfRoleCompositionCampaignInfo.to_json()

# convert the object into a dict
fullcampaign_all_of_role_composition_campaign_info_dict = fullcampaign_all_of_role_composition_campaign_info_instance.to_dict()
# create an instance of FullcampaignAllOfRoleCompositionCampaignInfo from a dict
fullcampaign_all_of_role_composition_campaign_info_form_dict = fullcampaign_all_of_role_composition_campaign_info.from_dict(fullcampaign_all_of_role_composition_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


