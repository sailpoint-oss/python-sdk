# CampaignFilterDetails

Campaign Filter Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the campaign filter | [optional] 
**name** | **str** | This is campaign filter&#39;s name. | 
**description** | **str** | This is campaign filter&#39;s description. | 
**owner** | **str** | The owner of this filter. This field is automatically populated at creation time with the current user. | 
**mode** | **object** | The mode/type of Filter, where it is of INCLUSION or EXCLUSION type. INCLUSION type will include the data in generated campaign  as per specified in criteria, whereas EXCLUSION type will exclude the the data in generated campaign as per specified in criteria. | 
**criteria_list** | [**List[CampaignFilterDetailsCriteriaListInner]**](CampaignFilterDetailsCriteriaListInner.md) | List of criteria. | [optional] 

## Example

```python
from sailpoint.v3.models.campaign_filter_details import CampaignFilterDetails

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


