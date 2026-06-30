---
id: inteloutlieraccessitem
title: Inteloutlieraccessitem
pagination_label: Inteloutlieraccessitem
sidebar_label: Inteloutlieraccessitem
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Inteloutlieraccessitem', 'Inteloutlieraccessitem'] 
slug: /tools/sdk/python/intelligence/models/inteloutlieraccessitem
tags: ['SDK', 'Software Development Kit', 'Inteloutlieraccessitem', 'Inteloutlieraccessitem']
---

# Inteloutlieraccessitem

One outlier access-item row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Stable identifier of the outlier access-item row. | [required]
**display_name** | **str** | Display label of the risky access item. | [required]
**description** | **str** | Optional descriptive text for the risky access item. | [optional] 
**access_type** | **str** | Access item type. | [required]
**source_name** | **str** | Source name where the risky access item exists. | [required]
**extremely_rare** | **bool** | Indicates whether analytics marked this item as extremely rare. | [required]
}

## Example

```python
from sailpoint.intelligence.models.inteloutlieraccessitem import Inteloutlieraccessitem

inteloutlieraccessitem = Inteloutlieraccessitem(
id='outlier-access-001',
display_name='Example_Admin_Access',
description='',
access_type='ENTITLEMENT',
source_name='Example SaaS Source',
extremely_rare=False
)

```
[[Back to top]](#) 

