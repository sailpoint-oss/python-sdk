---
id: campaign-report
title: CampaignReport
pagination_label: CampaignReport
sidebar_label: CampaignReport
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignReport', 'CampaignReport'] 
slug: /tools/sdk/python/gov-certification/models/campaign-report
tags: ['SDK', 'Software Development Kit', 'CampaignReport', 'CampaignReport']
---

# CampaignReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the campaign report. | [required]
**name** | **str** | The human readable report name | [required]
**campaign_id** | **str** | The unique ID of the campaign. | [required]
**type** | **CampaignReportType** |  | [required]
**format** | **CampaignReportFormat** |  | [required]
**created** | **datetime** | The date the report was created. | [required]
**modified** | **datetime** | The date the report was modified. | [optional] 
**status** | **CampaignReportStatus** |  | [required]
}

## Example

```python
from sailpoint.gov_certification.models.campaign_report import CampaignReport

campaign_report = CampaignReport(
id='e1aeb0b6-0021-4f40-8bc7-5c56533214b3',
name='ABC Campaign - Sign Off Report 2024-10-16_13:18UTC',
campaign_id='4e1aeef7-3742-40ea-920b-deeb8d20d7ee',
type='REMEDIATION',
format='PDF',
created='2018-10-19T13:49:37.385Z',
modified='2018-10-19T13:49:37.385Z',
status='IN_PROGRESS'
)

```
[[Back to top]](#) 

