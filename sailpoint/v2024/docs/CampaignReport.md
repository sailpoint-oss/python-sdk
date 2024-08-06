# CampaignReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | SOD policy violation report result DTO type. | [optional] 
**id** | **str** | SOD policy violation report result ID. | [optional] 
**name** | **str** | Human-readable name of the SOD policy violation report result. | [optional] 
**status** | **str** | Status of a SOD policy violation report. | [optional] 
**report_type** | [**ReportType**](ReportType.md) |  | 
**last_run_at** | **datetime** | The most recent date and time this report was run | [optional] [readonly] 

## Example

```python
from sailpoint.v2024.models.campaign_report import CampaignReport

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignReport from a JSON string
campaign_report_instance = CampaignReport.from_json(json)
# print the JSON string representation of the object
print CampaignReport.to_json()

# convert the object into a dict
campaign_report_dict = campaign_report_instance.to_dict()
# create an instance of CampaignReport from a dict
campaign_report_form_dict = campaign_report.from_dict(campaign_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


