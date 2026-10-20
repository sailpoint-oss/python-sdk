---
id: insight-details
title: InsightDetails
pagination_label: InsightDetails
sidebar_label: InsightDetails
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'InsightDetails', 'InsightDetails'] 
slug: /tools/sdk/python/gov-certification/models/insight-details
tags: ['SDK', 'Software Development Kit', 'InsightDetails', 'InsightDetails']
---

# InsightDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search query that selects the access included in the insight. | [optional] 
**identity_id_filter** | **[]str** | Identity IDs used to limit the insight to specific identities. | [optional] 
**type** | **ScopedAccessType** |  | [optional] 
**campaign_type** |  **Enum** [  'IDENTITY' ] | The type of search campaign. Can only be IDENTITY | [optional] 
}

## Example

```python
from sailpoint.gov_certification.models.insight_details import InsightDetails

insight_details = InsightDetails(
query='admin',
identity_id_filter=["2c918085718230600171993742c63558"],
type='ENTITLEMENT',
campaign_type='IDENTITY'
)

```
[[Back to top]](#) 

