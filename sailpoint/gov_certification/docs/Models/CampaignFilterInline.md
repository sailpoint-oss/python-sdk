---
id: campaign-filter-inline
title: CampaignFilterInline
pagination_label: CampaignFilterInline
sidebar_label: CampaignFilterInline
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignFilterInline', 'CampaignFilterInline'] 
slug: /tools/sdk/python/gov-certification/models/campaign-filter-inline
tags: ['SDK', 'Software Development Kit', 'CampaignFilterInline', 'CampaignFilterInline']
---

# CampaignFilterInline

Inline Campaign Filter Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **CampaignFilterType** |  | [required]
**criteria_list** | [**[]Criteria**](criteria) | List of criteria. | [required]
}

## Example

```python
from sailpoint.gov_certification.models.campaign_filter_inline import CampaignFilterInline

campaign_filter_inline = CampaignFilterInline(
mode='INCLUSION',
criteria_list=[{"criteriaType":"IDENTITY","criteriaProperty":"DISPLAY_NAME","criteriaValue":"support","operation":"EQUALS"}]
)

```
[[Back to top]](#) 

