---
id: campaign-filter-ref
title: CampaignFilterRef
pagination_label: CampaignFilterRef
sidebar_label: CampaignFilterRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignFilterRef', 'CampaignFilterRef'] 
slug: /tools/sdk/python/gov-certification/models/campaign-filter-ref
tags: ['SDK', 'Software Development Kit', 'CampaignFilterRef', 'CampaignFilterRef']
---

# CampaignFilterRef

Determines which items will be included in this campaign. The default campaign filter is used if this field is left blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of whatever type of filter is being used. | [required]
**name** | **str** | Name of the filter | [required]
}

## Example

```python
from sailpoint.gov_certification.models.campaign_filter_ref import CampaignFilterRef

campaign_filter_ref = CampaignFilterRef(
id='e9f9a139-7b84-2fd5-a658-42087040d3ac',
name='Test Filter'
)

```
[[Back to top]](#) 

