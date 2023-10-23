# CampaignReportsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attribute_columns** | **List[str]** | list of identity attribute columns | [optional] 

## Example

```python
from v3.models.campaign_reports_config import CampaignReportsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignReportsConfig from a JSON string
campaign_reports_config_instance = CampaignReportsConfig.from_json(json)
# print the JSON string representation of the object
print CampaignReportsConfig.to_json()

# convert the object into a dict
campaign_reports_config_dict = campaign_reports_config_instance.to_dict()
# create an instance of CampaignReportsConfig from a dict
campaign_reports_config_form_dict = campaign_reports_config.from_dict(campaign_reports_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


