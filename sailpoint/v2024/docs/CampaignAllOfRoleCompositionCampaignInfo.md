# CampaignAllOfRoleCompositionCampaignInfo

Optional configuration options for role composition campaigns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer** | [**CampaignAllOfSearchCampaignInfoReviewer**](CampaignAllOfSearchCampaignInfoReviewer.md) |  | [optional] 
**role_ids** | **List[str]** | Optional list of roles to include in this campaign. Only one of &#x60;roleIds&#x60; and &#x60;query&#x60; may be set; if neither are set, all roles are included. | [optional] 
**remediator_ref** | [**CampaignAllOfRoleCompositionCampaignInfoRemediatorRef**](CampaignAllOfRoleCompositionCampaignInfoRemediatorRef.md) |  | 
**query** | **str** | Optional search query to scope this campaign to a set of roles. Only one of &#x60;roleIds&#x60; and &#x60;query&#x60; may be set; if neither are set, all roles are included. | [optional] 
**description** | **str** | Describes this role composition campaign. Intended for storing the query used, and possibly the number of roles selected/available. | [optional] 

## Example

```python
from sailpoint.v2024.models.campaign_all_of_role_composition_campaign_info import CampaignAllOfRoleCompositionCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfRoleCompositionCampaignInfo from a JSON string
campaign_all_of_role_composition_campaign_info_instance = CampaignAllOfRoleCompositionCampaignInfo.from_json(json)
# print the JSON string representation of the object
print CampaignAllOfRoleCompositionCampaignInfo.to_json()

# convert the object into a dict
campaign_all_of_role_composition_campaign_info_dict = campaign_all_of_role_composition_campaign_info_instance.to_dict()
# create an instance of CampaignAllOfRoleCompositionCampaignInfo from a dict
campaign_all_of_role_composition_campaign_info_form_dict = campaign_all_of_role_composition_campaign_info.from_dict(campaign_all_of_role_composition_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


