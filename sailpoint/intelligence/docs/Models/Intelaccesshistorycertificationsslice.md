---
id: intelaccesshistorycertificationsslice
title: Intelaccesshistorycertificationsslice
pagination_label: Intelaccesshistorycertificationsslice
sidebar_label: Intelaccesshistorycertificationsslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelaccesshistorycertificationsslice', 'Intelaccesshistorycertificationsslice'] 
slug: /tools/sdk/python/intelligence/models/intelaccesshistorycertificationsslice
tags: ['SDK', 'Software Development Kit', 'Intelaccesshistorycertificationsslice', 'Intelaccesshistorycertificationsslice']
---

# Intelaccesshistorycertificationsslice

Certification history slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **[]Intelcertificationhistoryevent** | First page of certification history events for the identity. | [required]
**next** | **str** | Absolute URL to the next certifications page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelaccesshistorycertificationsslice import Intelaccesshistorycertificationsslice

intelaccesshistorycertificationsslice = Intelaccesshistorycertificationsslice(
items=[
                    { }
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history/certifications?limit=10&offset=10'
)

```
[[Back to top]](#) 

