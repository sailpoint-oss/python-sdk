# CampaignAllOfMachineAccountCampaignInfo

Must be set only if the campaign type is MACHINE_ACCOUNT.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[str]** | The list of sources to be included in the campaign. | [optional] 
**reviewer_type** | **str** | The reviewer&#39;s type. | [optional] 

## Example

```python
from sailpoint.v2024.models.campaign_all_of_machine_account_campaign_info import CampaignAllOfMachineAccountCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfMachineAccountCampaignInfo from a JSON string
campaign_all_of_machine_account_campaign_info_instance = CampaignAllOfMachineAccountCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(CampaignAllOfMachineAccountCampaignInfo.to_json())

# convert the object into a dict
campaign_all_of_machine_account_campaign_info_dict = campaign_all_of_machine_account_campaign_info_instance.to_dict()
# create an instance of CampaignAllOfMachineAccountCampaignInfo from a dict
campaign_all_of_machine_account_campaign_info_from_dict = CampaignAllOfMachineAccountCampaignInfo.from_dict(campaign_all_of_machine_account_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


