# CampaignAllOfFilter

Determines which items will be included in this campaign. The default campaign filter is used if this field is left blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of whatever type of filter is being used. | [optional] 
**type** | **str** | Type of the filter | [optional] 
**name** | **str** | Name of the filter | [optional] 

## Example

```python
from sailpoint.v3.models.campaign_all_of_filter import CampaignAllOfFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAllOfFilter from a JSON string
campaign_all_of_filter_instance = CampaignAllOfFilter.from_json(json)
# print the JSON string representation of the object
print CampaignAllOfFilter.to_json()

# convert the object into a dict
campaign_all_of_filter_dict = campaign_all_of_filter_instance.to_dict()
# create an instance of CampaignAllOfFilter from a dict
campaign_all_of_filter_form_dict = campaign_all_of_filter.from_dict(campaign_all_of_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


