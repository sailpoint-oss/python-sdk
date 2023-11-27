# CampaignFilterDetailsCriteriaListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CriteriaType**](CriteriaType.md) |  | 
**operation** | [**Operation**](Operation.md) |  | 
**var_property** | **str** | The specified key from the Type of criteria. | 
**value** | **str** | The value for the specified key from the Type of Criteria | 

## Example

```python
from sailpoint.v3.models.campaign_filter_details_criteria_list_inner import CampaignFilterDetailsCriteriaListInner

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignFilterDetailsCriteriaListInner from a JSON string
campaign_filter_details_criteria_list_inner_instance = CampaignFilterDetailsCriteriaListInner.from_json(json)
# print the JSON string representation of the object
print CampaignFilterDetailsCriteriaListInner.to_json()

# convert the object into a dict
campaign_filter_details_criteria_list_inner_dict = campaign_filter_details_criteria_list_inner_instance.to_dict()
# create an instance of CampaignFilterDetailsCriteriaListInner from a dict
campaign_filter_details_criteria_list_inner_form_dict = campaign_filter_details_criteria_list_inner.from_dict(campaign_filter_details_criteria_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


