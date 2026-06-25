---
id: intelidentityriskbody
title: Intelidentityriskbody
pagination_label: Intelidentityriskbody
sidebar_label: Intelidentityriskbody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentityriskbody', 'Intelidentityriskbody'] 
slug: /tools/sdk/python/intelligence-package/models/intelidentityriskbody
tags: ['SDK', 'Software Development Kit', 'Intelidentityriskbody', 'Intelidentityriskbody']
---

# Intelidentityriskbody

Shared response envelope for risk endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outliers** | [**[]Inteloutlieraccessitem**](inteloutlieraccessitem) | Page of outlier access-items associated with the resolved identity outlier. | [required]
**outliers_total** | **int** | Total available outlier access-item count from upstream. | [required]
**links** | [**Intelrisklinks**](intelrisklinks) | Continuation links map; omitted when no additional page exists. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package.models.intelidentityriskbody import Intelidentityriskbody

intelidentityriskbody = Intelidentityriskbody(
outliers=[{"id":"outlier-access-001","displayName":"Example_Admin_Access","description":null,"accessType":"ENTITLEMENT","sourceName":"Example SaaS Source","extremelyRare":false}],
outliers_total=312,
links=sailpoint.intelligence_package.models.intelrisklinks.intelrisklinks(
                    outliers = {"href":"https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/00000000000000000000000000000000/risk/outliers?limit=250&offset=250"}, )
)

```
[[Back to top]](#) 

