# CampaignGeneratedCampaignCampaignOwner

The identity that owns the campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity. | 
**display_name** | **str** | The display name of the identity. | 
**email** | **str** | The primary email address of the identity. | 

## Example

```python
from sailpoint.beta.models.campaign_generated_campaign_campaign_owner import CampaignGeneratedCampaignCampaignOwner

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignGeneratedCampaignCampaignOwner from a JSON string
campaign_generated_campaign_campaign_owner_instance = CampaignGeneratedCampaignCampaignOwner.from_json(json)
# print the JSON string representation of the object
print(CampaignGeneratedCampaignCampaignOwner.to_json())

# convert the object into a dict
campaign_generated_campaign_campaign_owner_dict = campaign_generated_campaign_campaign_owner_instance.to_dict()
# create an instance of CampaignGeneratedCampaignCampaignOwner from a dict
campaign_generated_campaign_campaign_owner_from_dict = CampaignGeneratedCampaignCampaignOwner.from_dict(campaign_generated_campaign_campaign_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


