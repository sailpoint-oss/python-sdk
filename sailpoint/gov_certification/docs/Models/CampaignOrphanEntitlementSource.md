---
id: campaign-orphan-entitlement-source
title: CampaignOrphanEntitlementSource
pagination_label: CampaignOrphanEntitlementSource
sidebar_label: CampaignOrphanEntitlementSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CampaignOrphanEntitlementSource', 'CampaignOrphanEntitlementSource'] 
slug: /tools/sdk/python/gov-certification/models/campaign-orphan-entitlement-source
tags: ['SDK', 'Software Development Kit', 'CampaignOrphanEntitlementSource', 'CampaignOrphanEntitlementSource']
---

# CampaignOrphanEntitlementSource

A source that has at least one orphan entitlement included in the campaign, as reported at staging time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'SOURCE' ] | Kind of reference; currently only SOURCE is used. | [required]
**id** | **str** | Identifier of the source. | [required]
**name** | **str** | Display name of the source. | [required]
}

## Example

```python
from sailpoint.gov_certification.models.campaign_orphan_entitlement_source import CampaignOrphanEntitlementSource

campaign_orphan_entitlement_source = CampaignOrphanEntitlementSource(
type='SOURCE',
id='30e6435e60bf47b0bc11622c31dfdbfd',
name='Active Directory'
)

```
[[Back to top]](#) 

