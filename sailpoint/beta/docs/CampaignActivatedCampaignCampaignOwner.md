# CampaignActivatedCampaignCampaignOwner

Details of the identity that owns the campaign.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the identity. | 
**display_name** | **str** | The human friendly name of the identity. | 
**email** | **str** | The primary email address of the identity. | 

## Example

```python
from beta.models.campaign_activated_campaign_campaign_owner import CampaignActivatedCampaignCampaignOwner

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignActivatedCampaignCampaignOwner from a JSON string
campaign_activated_campaign_campaign_owner_instance = CampaignActivatedCampaignCampaignOwner.from_json(json)
# print the JSON string representation of the object
print CampaignActivatedCampaignCampaignOwner.to_json()

# convert the object into a dict
campaign_activated_campaign_campaign_owner_dict = campaign_activated_campaign_campaign_owner_instance.to_dict()
# create an instance of CampaignActivatedCampaignCampaignOwner from a dict
campaign_activated_campaign_campaign_owner_form_dict = campaign_activated_campaign_campaign_owner.from_dict(campaign_activated_campaign_campaign_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


