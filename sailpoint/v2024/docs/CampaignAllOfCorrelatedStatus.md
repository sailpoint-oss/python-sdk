# CampaignAllOfCorrelatedStatus

The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.v2024.models.campaign_all_of_correlated_status import CampaignAllOfCorrelatedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfCorrelatedStatus from a JSON string
campaign_all_of_correlated_status_instance = CampaignAllOfCorrelatedStatus.from_json(json)
# print the JSON string representation of the object
print(CampaignAllOfCorrelatedStatus.to_json())

# convert the object into a dict
campaign_all_of_correlated_status_dict = campaign_all_of_correlated_status_instance.to_dict()
# create an instance of CampaignAllOfCorrelatedStatus from a dict
campaign_all_of_correlated_status_from_dict = CampaignAllOfCorrelatedStatus.from_dict(campaign_all_of_correlated_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


