# CampaignAllOfSourceOwnerCampaignInfo

Must be set only if the campaign type is SOURCE_OWNER.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[str]** | The list of sources to be included in the campaign. | [optional] 

## Example

```python
from sailpoint.v3.models.campaign_all_of_source_owner_campaign_info import CampaignAllOfSourceOwnerCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfSourceOwnerCampaignInfo from a JSON string
campaign_all_of_source_owner_campaign_info_instance = CampaignAllOfSourceOwnerCampaignInfo.from_json(json)
# print the JSON string representation of the object
print CampaignAllOfSourceOwnerCampaignInfo.to_json()

# convert the object into a dict
campaign_all_of_source_owner_campaign_info_dict = campaign_all_of_source_owner_campaign_info_instance.to_dict()
# create an instance of CampaignAllOfSourceOwnerCampaignInfo from a dict
campaign_all_of_source_owner_campaign_info_form_dict = campaign_all_of_source_owner_campaign_info.from_dict(campaign_all_of_source_owner_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


