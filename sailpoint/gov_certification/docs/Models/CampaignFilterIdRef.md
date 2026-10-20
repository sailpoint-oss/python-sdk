---
id: campaign-filter-id-ref
title: CampaignFilterIdRef
pagination_label: CampaignFilterIdRef
sidebar_label: CampaignFilterIdRef
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignFilterIdRef', 'CampaignFilterIdRef'] 
slug: /tools/sdk/python/gov-certification/models/campaign-filter-id-ref
tags: ['SDK', 'Software Development Kit', 'CampaignFilterIdRef', 'CampaignFilterIdRef']
---

# CampaignFilterIdRef

Determines which items will be included in this campaign. The default campaign filter is used if this field is left blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of whatever type of filter is being used. | [required]
}

## Example

```python
from sailpoint.gov_certification.models.campaign_filter_id_ref import CampaignFilterIdRef

campaign_filter_id_ref = CampaignFilterIdRef(
id='e9f9a139-7b84-2fd5-a658-42087040d3ac'
)

```
[[Back to top]](#) 

