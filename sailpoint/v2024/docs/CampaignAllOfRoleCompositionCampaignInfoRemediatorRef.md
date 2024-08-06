# CampaignAllOfRoleCompositionCampaignInfoRemediatorRef

This determines who remediation tasks will be assigned to. Remediation tasks are created for each revoke decision on items in the campaign. The only legal remediator type is 'IDENTITY', and the chosen identity must be a Role Admin or Org Admin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Legal Remediator Type | 
**id** | **str** | The ID of the remediator. | 
**name** | **str** | The name of the remediator. | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.campaign_all_of_role_composition_campaign_info_remediator_ref import CampaignAllOfRoleCompositionCampaignInfoRemediatorRef

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfRoleCompositionCampaignInfoRemediatorRef from a JSON string
campaign_all_of_role_composition_campaign_info_remediator_ref_instance = CampaignAllOfRoleCompositionCampaignInfoRemediatorRef.from_json(json)
# print the JSON string representation of the object
print CampaignAllOfRoleCompositionCampaignInfoRemediatorRef.to_json()

# convert the object into a dict
campaign_all_of_role_composition_campaign_info_remediator_ref_dict = campaign_all_of_role_composition_campaign_info_remediator_ref_instance.to_dict()
# create an instance of CampaignAllOfRoleCompositionCampaignInfoRemediatorRef from a dict
campaign_all_of_role_composition_campaign_info_remediator_ref_form_dict = campaign_all_of_role_composition_campaign_info_remediator_ref.from_dict(campaign_all_of_role_composition_campaign_info_remediator_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


