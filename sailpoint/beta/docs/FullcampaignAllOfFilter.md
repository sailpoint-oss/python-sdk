# FullcampaignAllOfFilter

Determines which items will be included in this campaign. The default campaign filter is used if this field is left blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of whatever type of filter is being used. | [optional] 
**type** | **str** | Type of the filter | [optional] 
**name** | **str** | Name of the filter | [optional] 

## Example

```python
from sailpoint.beta.models.fullcampaign_all_of_filter import FullcampaignAllOfFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FullcampaignAllOfFilter from a JSON string
fullcampaign_all_of_filter_instance = FullcampaignAllOfFilter.from_json(json)
# print the JSON string representation of the object
print(FullcampaignAllOfFilter.to_json())

# convert the object into a dict
fullcampaign_all_of_filter_dict = fullcampaign_all_of_filter_instance.to_dict()
# create an instance of FullcampaignAllOfFilter from a dict
fullcampaign_all_of_filter_from_dict = FullcampaignAllOfFilter.from_dict(fullcampaign_all_of_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


