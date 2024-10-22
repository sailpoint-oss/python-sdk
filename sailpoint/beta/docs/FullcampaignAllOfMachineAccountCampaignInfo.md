# FullcampaignAllOfMachineAccountCampaignInfo

Must be set only if the campaign type is MACHINE_ACCOUNT.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[str]** | The list of sources to be included in the campaign. | [optional] 
**reviewer_type** | **str** | The reviewer&#39;s type. | [optional] 

## Example

```python
from sailpoint.beta.models.fullcampaign_all_of_machine_account_campaign_info import FullcampaignAllOfMachineAccountCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfMachineAccountCampaignInfo from a JSON string
fullcampaign_all_of_machine_account_campaign_info_instance = FullcampaignAllOfMachineAccountCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(FullcampaignAllOfMachineAccountCampaignInfo.to_json())

# convert the object into a dict
fullcampaign_all_of_machine_account_campaign_info_dict = fullcampaign_all_of_machine_account_campaign_info_instance.to_dict()
# create an instance of FullcampaignAllOfMachineAccountCampaignInfo from a dict
fullcampaign_all_of_machine_account_campaign_info_from_dict = FullcampaignAllOfMachineAccountCampaignInfo.from_dict(fullcampaign_all_of_machine_account_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


