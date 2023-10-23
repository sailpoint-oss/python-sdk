# CampaignReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the campaign. | 
**name** | **str** | The name of the campaign. | 
**type** | **str** | The type of object that is being referenced. | 
**campaign_type** | **str** | The type of the campaign. | 
**description** | **str** | The description of the campaign set by the admin who created it. | 
**correlated_status** | **object** | The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source). | 
**mandatory_comment_requirement** | **str** | Determines whether comments are required for decisions during certification reviews. You can require comments for all decisions, revoke-only decisions, or no decisions. By default, comments are not required for decisions. | 

## Example

```python
from beta.models.campaign_reference import CampaignReference

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignReference from a JSON string
campaign_reference_instance = CampaignReference.from_json(json)
# print the JSON string representation of the object
print CampaignReference.to_json()

# convert the object into a dict
campaign_reference_dict = campaign_reference_instance.to_dict()
# create an instance of CampaignReference from a dict
campaign_reference_form_dict = campaign_reference.from_dict(campaign_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


