---
id: intel-access-history-certifications-slice
title: IntelAccessHistoryCertificationsSlice
pagination_label: IntelAccessHistoryCertificationsSlice
sidebar_label: IntelAccessHistoryCertificationsSlice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelAccessHistoryCertificationsSlice', 'IntelAccessHistoryCertificationsSlice'] 
slug: /tools/sdk/python/intelligence/models/intel-access-history-certifications-slice
tags: ['SDK', 'Software Development Kit', 'IntelAccessHistoryCertificationsSlice', 'IntelAccessHistoryCertificationsSlice']
---

# IntelAccessHistoryCertificationsSlice

Certification history slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **[]IntelCertificationHistoryEvent** | First page of certification history events for the identity. | [required]
**next** | **str** | Absolute URL to the next certifications page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intel_access_history_certifications_slice import IntelAccessHistoryCertificationsSlice

intel_access_history_certifications_slice = IntelAccessHistoryCertificationsSlice(
items=[
                    { }
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/intelligence/identities/v1/ef38f94347e94562b5bb8424a56397d8/access-history/certifications?limit=10&offset=10'
)

```
[[Back to top]](#) 

