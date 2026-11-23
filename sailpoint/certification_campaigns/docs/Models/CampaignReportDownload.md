---
id: campaign-report-download
title: CampaignReportDownload
pagination_label: CampaignReportDownload
sidebar_label: CampaignReportDownload
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignReportDownload', 'CampaignReportDownload'] 
slug: /tools/sdk/python/certification-campaigns/models/campaign-report-download
tags: ['SDK', 'Software Development Kit', 'CampaignReportDownload', 'CampaignReportDownload']
---

# CampaignReportDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the campaign report. | [required]
**download_url** | **str** | A URL to download the campaign report. A presigned download URL is valid for 90 minutes from the time it is returned. Call this endpoint again to get a new URL.  | [required]
}

## Example

```python
from sailpoint.certification_campaigns.models.campaign_report_download import CampaignReportDownload

campaign_report_download = CampaignReportDownload(
id='e1aeb0b600214f408bc75c56533214b3',
download_url='https://secure-content.accessiq.sailpoint.com/someCampaignReport.pdf'
)

```
[[Back to top]](#) 

