---
id: campaign-reports-config
title: CampaignReportsConfig
pagination_label: CampaignReportsConfig
sidebar_label: CampaignReportsConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignReportsConfig', 'CampaignReportsConfig'] 
slug: /tools/sdk/python/certification-campaigns/models/campaign-reports-config
tags: ['SDK', 'Software Development Kit', 'CampaignReportsConfig', 'CampaignReportsConfig']
---

# CampaignReportsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_attribute_columns** | **[]str** | list of identity attribute columns | [optional] 
}

## Example

```python
from sailpoint.certification_campaigns.models.campaign_reports_config import CampaignReportsConfig

campaign_reports_config = CampaignReportsConfig(
identity_attribute_columns=["firstname","lastname"]
)

```
[[Back to top]](#) 

