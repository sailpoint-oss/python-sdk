# CampaignTemplate

Campaign Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the campaign template | [optional] 
**name** | **str** | This template&#39;s name. Has no bearing on generated campaigns&#39; names. | 
**description** | **str** | This template&#39;s description. Has no bearing on generated campaigns&#39; descriptions. | 
**created** | **datetime** | Creation date of Campaign Template | [readonly] 
**modified** | **datetime** | Modification date of Campaign Template | [readonly] 
**scheduled** | **bool** | Indicates if this campaign template has been scheduled. | [optional] [readonly] [default to False]
**owner_ref** | [**CampaignTemplateOwnerRef**](CampaignTemplateOwnerRef.md) |  | [optional] 
**deadline_duration** | **str** | The time period during which the campaign should be completed, formatted as an ISO-8601 Duration. When this template generates a campaign, the campaign&#39;s deadline will be the current date plus this duration. For example, if generation occurred on 2020-01-01 and this field was \&quot;P2W\&quot; (two weeks), the resulting campaign&#39;s deadline would be 2020-01-15 (the current date plus 14 days). | [optional] 
**campaign** | [**Campaign**](.md) | This will hold campaign related information like name, description etc. | 

## Example

```python
from sailpoint.v3.models.campaign_template import CampaignTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTemplate from a JSON string
campaign_template_instance = CampaignTemplate.from_json(json)
# print the JSON string representation of the object
print CampaignTemplate.to_json()

# convert the object into a dict
campaign_template_dict = campaign_template_instance.to_dict()
# create an instance of CampaignTemplate from a dict
campaign_template_form_dict = campaign_template.from_dict(campaign_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


