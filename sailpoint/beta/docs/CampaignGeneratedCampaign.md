# CampaignGeneratedCampaign

Details about the campaign that was generated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the campaign. | 
**name** | **str** | Human friendly name of the campaign. | 
**description** | **str** | Extended description of the campaign. | 
**created** | **datetime** | The date and time the campaign was created. | 
**modified** | **str** | The date and time the campaign was last modified. | [optional] 
**deadline** | **str** | The date and time when the campaign must be finished by. | [optional] 
**type** | **object** | The type of campaign that was generated. | 
**campaign_owner** | [**CampaignGeneratedCampaignCampaignOwner**](CampaignGeneratedCampaignCampaignOwner.md) |  | 
**status** | **object** | The current status of the campaign. | 

## Example

```python
from beta.models.campaign_generated_campaign import CampaignGeneratedCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignGeneratedCampaign from a JSON string
campaign_generated_campaign_instance = CampaignGeneratedCampaign.from_json(json)
# print the JSON string representation of the object
print CampaignGeneratedCampaign.to_json()

# convert the object into a dict
campaign_generated_campaign_dict = campaign_generated_campaign_instance.to_dict()
# create an instance of CampaignGeneratedCampaign from a dict
campaign_generated_campaign_form_dict = campaign_generated_campaign.from_dict(campaign_generated_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


