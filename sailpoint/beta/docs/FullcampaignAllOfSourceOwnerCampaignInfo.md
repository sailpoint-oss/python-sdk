# FullcampaignAllOfSourceOwnerCampaignInfo

Must be set only if the campaign type is SOURCE_OWNER.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[str]** | The list of sources to be included in the campaign. | [optional] 

## Example

```python
from sailpoint.beta.models.fullcampaign_all_of_source_owner_campaign_info import FullcampaignAllOfSourceOwnerCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfSourceOwnerCampaignInfo from a JSON string
fullcampaign_all_of_source_owner_campaign_info_instance = FullcampaignAllOfSourceOwnerCampaignInfo.from_json(json)
# print the JSON string representation of the object
print FullcampaignAllOfSourceOwnerCampaignInfo.to_json()

# convert the object into a dict
fullcampaign_all_of_source_owner_campaign_info_dict = fullcampaign_all_of_source_owner_campaign_info_instance.to_dict()
# create an instance of FullcampaignAllOfSourceOwnerCampaignInfo from a dict
fullcampaign_all_of_source_owner_campaign_info_form_dict = fullcampaign_all_of_source_owner_campaign_info.from_dict(fullcampaign_all_of_source_owner_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


