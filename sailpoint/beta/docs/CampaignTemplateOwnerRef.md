# CampaignTemplateOwnerRef

The owner of this template, and the owner of campaigns generated from this template via a schedule. This field is automatically populated at creation time with the current user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the owner | [optional] 
**type** | **str** | Type of the owner | [optional] 
**name** | **str** | Name of the owner | [optional] 
**email** | **str** | Email of the owner | [optional] 

## Example

```python
from sailpoint.beta.models.campaign_template_owner_ref import CampaignTemplateOwnerRef

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignTemplateOwnerRef from a JSON string
campaign_template_owner_ref_instance = CampaignTemplateOwnerRef.from_json(json)
# print the JSON string representation of the object
print CampaignTemplateOwnerRef.to_json()

# convert the object into a dict
campaign_template_owner_ref_dict = campaign_template_owner_ref_instance.to_dict()
# create an instance of CampaignTemplateOwnerRef from a dict
campaign_template_owner_ref_form_dict = campaign_template_owner_ref.from_dict(campaign_template_owner_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


