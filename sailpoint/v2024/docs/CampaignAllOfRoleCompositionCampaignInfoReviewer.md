# CampaignAllOfRoleCompositionCampaignInfoReviewer

If specified, this identity or governance group will be the reviewer for all certifications in this campaign. The allowed DTO types are IDENTITY and GOVERNANCE_GROUP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The reviewer&#39;s DTO type. | [optional] 
**id** | **str** | The reviewer&#39;s ID. | [optional] 
**name** | **str** | The reviewer&#39;s name. | [optional] 

## Example

```python
from sailpoint.v2024.models.campaign_all_of_role_composition_campaign_info_reviewer import CampaignAllOfRoleCompositionCampaignInfoReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfRoleCompositionCampaignInfoReviewer from a JSON string
campaign_all_of_role_composition_campaign_info_reviewer_instance = CampaignAllOfRoleCompositionCampaignInfoReviewer.from_json(json)
# print the JSON string representation of the object
print(CampaignAllOfRoleCompositionCampaignInfoReviewer.to_json())

# convert the object into a dict
campaign_all_of_role_composition_campaign_info_reviewer_dict = campaign_all_of_role_composition_campaign_info_reviewer_instance.to_dict()
# create an instance of CampaignAllOfRoleCompositionCampaignInfoReviewer from a dict
campaign_all_of_role_composition_campaign_info_reviewer_from_dict = CampaignAllOfRoleCompositionCampaignInfoReviewer.from_dict(campaign_all_of_role_composition_campaign_info_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


