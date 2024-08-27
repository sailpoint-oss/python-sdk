# ActivateCampaignOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | The timezone must be in a valid ISO 8601 format. Timezones in ISO 8601 are represented as UTC (represented as &#39;Z&#39;) or as an offset from UTC. The offset format can be +/-hh:mm, +/-hhmm, or +/-hh. | [optional] [default to 'Z']

## Example

```python
from sailpoint.beta.models.activate_campaign_options import ActivateCampaignOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateCampaignOptions from a JSON string
activate_campaign_options_instance = ActivateCampaignOptions.from_json(json)
# print the JSON string representation of the object
print(ActivateCampaignOptions.to_json())

# convert the object into a dict
activate_campaign_options_dict = activate_campaign_options_instance.to_dict()
# create an instance of ActivateCampaignOptions from a dict
activate_campaign_options_from_dict = ActivateCampaignOptions.from_dict(activate_campaign_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


