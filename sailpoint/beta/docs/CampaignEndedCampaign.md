# CampaignEndedCampaign

Details about the certification campaign that ended.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for the campaign. | 
**name** | **str** | The human friendly name of the campaign. | 
**description** | **str** | Extended description of the campaign. | 
**created** | **datetime** | The date and time the campaign was created. | 
**modified** | **datetime** | The date and time the campaign was last modified. | [optional] 
**deadline** | **datetime** | The date and time the campaign is due. | 
**type** | **object** | The type of campaign. | 
**campaign_owner** | [**CampaignActivatedCampaignCampaignOwner**](CampaignActivatedCampaignCampaignOwner.md) |  | 
**status** | **object** | The current status of the campaign. | 

## Example

```python
from beta.models.campaign_ended_campaign import CampaignEndedCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignEndedCampaign from a JSON string
campaign_ended_campaign_instance = CampaignEndedCampaign.from_json(json)
# print the JSON string representation of the object
print CampaignEndedCampaign.to_json()

# convert the object into a dict
campaign_ended_campaign_dict = campaign_ended_campaign_instance.to_dict()
# create an instance of CampaignEndedCampaign from a dict
campaign_ended_campaign_form_dict = campaign_ended_campaign.from_dict(campaign_ended_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


