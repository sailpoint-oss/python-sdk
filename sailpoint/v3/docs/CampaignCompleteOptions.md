# CampaignCompleteOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_action** | **str** | Determines whether to auto-approve(APPROVE) or auto-revoke(REVOKE) upon campaign completion. | [optional] [default to 'APPROVE']

## Example

```python
from sailpoint.v3.models.campaign_complete_options import CampaignCompleteOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignCompleteOptions from a JSON string
campaign_complete_options_instance = CampaignCompleteOptions.from_json(json)
# print the JSON string representation of the object
print(CampaignCompleteOptions.to_json())

# convert the object into a dict
campaign_complete_options_dict = campaign_complete_options_instance.to_dict()
# create an instance of CampaignCompleteOptions from a dict
campaign_complete_options_from_dict = CampaignCompleteOptions.from_dict(campaign_complete_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


