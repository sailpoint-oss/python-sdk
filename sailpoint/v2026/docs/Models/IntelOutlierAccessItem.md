---
id: v2026-intel-outlier-access-item
title: IntelOutlierAccessItem
pagination_label: IntelOutlierAccessItem
sidebar_label: IntelOutlierAccessItem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelOutlierAccessItem', 'V2026IntelOutlierAccessItem'] 
slug: /tools/sdk/python/v2026/models/intel-outlier-access-item
tags: ['SDK', 'Software Development Kit', 'IntelOutlierAccessItem', 'V2026IntelOutlierAccessItem']
---

# IntelOutlierAccessItem

One outlier access-item row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stable identifier of the outlier access-item row. | [required]
**display_name** | **str** | Display label of the risky access item. | [required]
**description** | **str** | Optional descriptive text for the risky access item. | [optional] 
**access_type** | **str** | Access item type (for example ENTITLEMENT, ROLE, ACCESS_PROFILE, ACCOUNT, or APP). | [required]
**source_name** | **str** | Source name where the risky access item exists. | [required]
**extremely_rare** | **bool** | Indicates whether analytics marked this item as extremely rare. | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_outlier_access_item import IntelOutlierAccessItem

intel_outlier_access_item = IntelOutlierAccessItem(
id='outlier-access-001',
display_name='Example_Admin_Access',
description='',
access_type='ENTITLEMENT',
source_name='Example SaaS Source',
extremely_rare=False
)

```
[[Back to top]](#) 

