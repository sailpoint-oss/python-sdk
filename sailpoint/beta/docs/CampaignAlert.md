# CampaignAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Denotes the level of the message | [optional] 
**localizations** | [**List[ErrorMessageDto]**](ErrorMessageDto.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.campaign_alert import CampaignAlert

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAlert from a JSON string
campaign_alert_instance = CampaignAlert.from_json(json)
# print the JSON string representation of the object
print CampaignAlert.to_json()

# convert the object into a dict
campaign_alert_dict = campaign_alert_instance.to_dict()
# create an instance of CampaignAlert from a dict
campaign_alert_form_dict = campaign_alert.from_dict(campaign_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


