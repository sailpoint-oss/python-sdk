# GetActiveCampaigns200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the campaign | [optional] [readonly] 
**name** | **str** | The campaign name. If this object is part of a template, special formatting applies; see the &#x60;/campaign-templates/{id}/generate&#x60; endpoint documentation for details.  | 
**description** | **str** | The campaign description. If this object is part of a template, special formatting applies; see the &#x60;/campaign-templates/{id}/generate&#x60; endpoint documentation for details.  | 
**deadline** | **datetime** | The campaign&#39;s completion deadline.  This date must be in the future in order to activate the campaign.  If you try to activate a campaign with a deadline of today or in the past, you will receive a 400 error response. | [optional] 
**type** | **str** | The type of campaign. Could be extended in the future. | 
**email_notification_enabled** | **bool** | Enables email notification for this campaign | [optional] [default to False]
**auto_revoke_allowed** | **bool** | Allows auto revoke for this campaign | [optional] [default to False]
**recommendations_enabled** | **bool** | Enables IAI for this campaign. Accepts true even if the IAI product feature is off. If IAI is turned off then campaigns generated from this template will indicate false. The real value will then be returned if IAI is ever enabled for the org in the future.  | [optional] [default to False]
**status** | **str** | The campaign&#39;s current status. | [optional] [readonly] 
**correlated_status** | **str** | The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source). | [optional] 
**created** | **datetime** | Created time of the campaign | [optional] [readonly] 
**total_certifications** | **int** | The total number of certifications in this campaign. | [optional] [readonly] 
**completed_certifications** | **int** | The number of completed certifications in this campaign. | [optional] [readonly] 
**alerts** | [**List[CampaignAlert]**](CampaignAlert.md) | A list of errors and warnings that have accumulated. | [optional] [readonly] 
**modified** | **datetime** | Modified time of the campaign | [optional] [readonly] 
**filter** | [**FullcampaignAllOfFilter**](FullcampaignAllOfFilter.md) |  | [optional] 
**sunset_comments_required** | **bool** | Determines if comments on sunset date changes are required. | [optional] [default to True]
**source_owner_campaign_info** | [**FullcampaignAllOfSourceOwnerCampaignInfo**](FullcampaignAllOfSourceOwnerCampaignInfo.md) |  | [optional] 
**search_campaign_info** | [**FullcampaignAllOfSearchCampaignInfo**](FullcampaignAllOfSearchCampaignInfo.md) |  | [optional] 
**role_composition_campaign_info** | [**FullcampaignAllOfRoleCompositionCampaignInfo**](FullcampaignAllOfRoleCompositionCampaignInfo.md) |  | [optional] 
**machine_account_campaign_info** | [**FullcampaignAllOfMachineAccountCampaignInfo**](FullcampaignAllOfMachineAccountCampaignInfo.md) |  | [optional] 
**sources_with_orphan_entitlements** | [**List[FullcampaignAllOfSourcesWithOrphanEntitlements]**](FullcampaignAllOfSourcesWithOrphanEntitlements.md) | A list of sources in the campaign that contain \\\&quot;orphan entitlements\\\&quot; (entitlements without a corresponding Managed Attribute). An empty list indicates the campaign has no orphan entitlements. Null indicates there may be unknown orphan entitlements in the campaign (the campaign was created before this feature was implemented). | [optional] [readonly] 
**mandatory_comment_requirement** | **str** | Determines whether comments are required for decisions during certification reviews. You can require comments for all decisions, revoke-only decisions, or no decisions. By default, comments are not required for decisions. | [optional] 

## Example

```python
from sailpoint.beta.models.get_active_campaigns200_response_inner import GetActiveCampaigns200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetActiveCampaigns200ResponseInner from a JSON string
get_active_campaigns200_response_inner_instance = GetActiveCampaigns200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetActiveCampaigns200ResponseInner.to_json())

# convert the object into a dict
get_active_campaigns200_response_inner_dict = get_active_campaigns200_response_inner_instance.to_dict()
# create an instance of GetActiveCampaigns200ResponseInner from a dict
get_active_campaigns200_response_inner_from_dict = GetActiveCampaigns200ResponseInner.from_dict(get_active_campaigns200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


