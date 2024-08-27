# SlimCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the campaign | [optional] [readonly] 
**name** | **str** | The campaign name. If this object is part of a template, special formatting applies; see the &#x60;/campaign-templates/{id}/generate&#x60; endpoint documentation for details. | 
**description** | **str** | The campaign description. If this object is part of a template, special formatting applies; see the &#x60;/campaign-templates/{id}/generate&#x60; endpoint documentation for details. | 
**deadline** | **datetime** | The campaign&#39;s completion deadline.  This date must be in the future in order to activate the campaign.  If you try to activate a campaign with a deadline of today or in the past, you will receive a 400 error response. | [optional] 
**type** | **str** | The type of campaign. Could be extended in the future. | 
**email_notification_enabled** | **bool** | Enables email notification for this campaign | [optional] [default to False]
**auto_revoke_allowed** | **bool** | Allows auto revoke for this campaign | [optional] [default to False]
**recommendations_enabled** | **bool** | Enables IAI for this campaign. Accepts true even if the IAI product feature is off. If IAI is turned off then campaigns generated from this template will indicate false. The real value will then be returned if IAI is ever enabled for the org in the future. | [optional] [default to False]
**status** | **str** | The campaign&#39;s current status. | [optional] [readonly] 
**correlated_status** | **str** | The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source). | [optional] 
**created** | **datetime** | Created time of the campaign | [optional] [readonly] 
**total_certifications** | **int** | The total number of certifications in this campaign. | [optional] [readonly] 
**completed_certifications** | **int** | The number of completed certifications in this campaign. | [optional] [readonly] 
**alerts** | [**List[CampaignAlert]**](CampaignAlert.md) | A list of errors and warnings that have accumulated. | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.slim_campaign import SlimCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of SlimCampaign from a JSON string
slim_campaign_instance = SlimCampaign.from_json(json)
# print the JSON string representation of the object
print(SlimCampaign.to_json())

# convert the object into a dict
slim_campaign_dict = slim_campaign_instance.to_dict()
# create an instance of SlimCampaign from a dict
slim_campaign_from_dict = SlimCampaign.from_dict(slim_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


