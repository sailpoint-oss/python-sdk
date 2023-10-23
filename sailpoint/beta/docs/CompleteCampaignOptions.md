# CompleteCampaignOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_complete_action** | **str** | Determines whether to auto-approve(APPROVE) or auto-revoke(REVOKE) upon campaign completion. | [optional] [default to 'APPROVE']

## Example

```python
from beta.models.complete_campaign_options import CompleteCampaignOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteCampaignOptions from a JSON string
complete_campaign_options_instance = CompleteCampaignOptions.from_json(json)
# print the JSON string representation of the object
print CompleteCampaignOptions.to_json()

# convert the object into a dict
complete_campaign_options_dict = complete_campaign_options_instance.to_dict()
# create an instance of CompleteCampaignOptions from a dict
complete_campaign_options_form_dict = complete_campaign_options.from_dict(complete_campaign_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


