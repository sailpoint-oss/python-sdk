# CampaignFilterDetails

Campaign Filter Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign filter name. | 
**description** | **str** | Campaign filter description. | [optional] 
**owner** | **str** | Owner of the filter. This field automatically populates at creation time with the current user. | 
**mode** | **object** | Mode/type of filter, either the INCLUSION or EXCLUSION type. The INCLUSION type includes the data in generated campaigns  as per specified in the criteria, whereas the EXCLUSION type excludes the data in generated campaigns as per specified in criteria. | 
**criteria_list** | [**List[CampaignFilterDetailsCriteriaListInner]**](CampaignFilterDetailsCriteriaListInner.md) | List of criteria. | [optional] 

## Example

```python
from sailpoint.v2024.models.campaign_filter_details import CampaignFilterDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignFilterDetails from a JSON string
campaign_filter_details_instance = CampaignFilterDetails.from_json(json)
# print the JSON string representation of the object
print CampaignFilterDetails.to_json()

# convert the object into a dict
campaign_filter_details_dict = campaign_filter_details_instance.to_dict()
# create an instance of CampaignFilterDetails from a dict
campaign_filter_details_form_dict = campaign_filter_details.from_dict(campaign_filter_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


