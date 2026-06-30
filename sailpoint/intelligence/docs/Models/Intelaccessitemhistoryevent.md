---
id: intelaccessitemhistoryevent
title: Intelaccessitemhistoryevent
pagination_label: Intelaccessitemhistoryevent
sidebar_label: Intelaccessitemhistoryevent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelaccessitemhistoryevent', 'Intelaccessitemhistoryevent'] 
slug: /tools/sdk/python/intelligence/models/intelaccessitemhistoryevent
tags: ['SDK', 'Software Development Kit', 'Intelaccessitemhistoryevent', 'Intelaccessitemhistoryevent']
---

# Intelaccessitemhistoryevent

Access-item history event. Supported eventTypes are AccessItemAssociated, AccessItemRemoved, and AccountStatusChanged. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** |  **Enum** [  'AccessItemAssociated',    'AccessItemRemoved',    'AccountStatusChanged' ] | Type of access-item history event. | [required]
**date_time** | **datetime** | Event timestamp. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelaccessitemhistoryevent import Intelaccessitemhistoryevent

intelaccessitemhistoryevent = Intelaccessitemhistoryevent(
event_type='AccessItemRemoved',
date_time='2026-05-11T09:40:04.496Z'
)

```
[[Back to top]](#) 

