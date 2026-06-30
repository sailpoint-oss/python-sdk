---
id: intelaccesshistoryaccessitemsslice
title: Intelaccesshistoryaccessitemsslice
pagination_label: Intelaccesshistoryaccessitemsslice
sidebar_label: Intelaccesshistoryaccessitemsslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelaccesshistoryaccessitemsslice', 'Intelaccesshistoryaccessitemsslice'] 
slug: /tools/sdk/python/intelligence/models/intelaccesshistoryaccessitemsslice
tags: ['SDK', 'Software Development Kit', 'Intelaccesshistoryaccessitemsslice', 'Intelaccesshistoryaccessitemsslice']
---

# Intelaccesshistoryaccessitemsslice

Access-item history slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **[]Intelaccessitemhistoryevent** | First page of access-item history events for the identity. | [required]
**next** | **str** | Absolute URL to the next access-items page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelaccesshistoryaccessitemsslice import Intelaccesshistoryaccessitemsslice

intelaccesshistoryaccessitemsslice = Intelaccesshistoryaccessitemsslice(
items=[
                    { }
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history/access-items?limit=10&offset=10'
)

```
[[Back to top]](#) 

