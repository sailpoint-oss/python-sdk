---
id: intelaccesshistory
title: Intelaccesshistory
pagination_label: Intelaccesshistory
sidebar_label: Intelaccesshistory
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelaccesshistory', 'Intelaccesshistory'] 
slug: /tools/sdk/python/intelligence/models/intelaccesshistory
tags: ['SDK', 'Software Development Kit', 'Intelaccesshistory', 'Intelaccesshistory']
---

# Intelaccesshistory

Access-history split into two independently paged categories. accessItems carries grant, remove, and account-status events. certifications carries identity-certified events. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_items** | [**Intelaccesshistoryaccessitemsslice**](intelaccesshistoryaccessitemsslice) | First page of access-item history events for the identity. | [required]
**certifications** | [**Intelaccesshistorycertificationsslice**](intelaccesshistorycertificationsslice) | First page of certification history events for the identity. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelaccesshistory import Intelaccesshistory

intelaccesshistory = Intelaccesshistory(
access_items=sailpoint.intelligence.models.intelaccesshistoryaccessitemsslice.intelaccesshistoryaccessitemsslice(
                    items = [
                        { }
                        ], 
                    next = 'https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history/access-items?limit=10&offset=10', ),
certifications=sailpoint.intelligence.models.intelaccesshistorycertificationsslice.intelaccesshistorycertificationsslice(
                    items = [
                        { }
                        ], 
                    next = 'https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history/certifications?limit=10&offset=10', )
)

```
[[Back to top]](#) 

