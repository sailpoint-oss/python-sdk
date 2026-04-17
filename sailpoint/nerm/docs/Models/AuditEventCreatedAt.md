---
id: audit-event-created-at
title: AuditEventCreatedAt
pagination_label: AuditEventCreatedAt
sidebar_label: AuditEventCreatedAt
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AuditEventCreatedAt', 'AuditEventCreatedAt'] 
slug: /tools/sdk/python//models/audit-event-created-at
tags: ['SDK', 'Software Development Kit', 'AuditEventCreatedAt', 'AuditEventCreatedAt']
---

# AuditEventCreatedAt

Search for record based on the created_at date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gt** | **date** | Greater Than - search for events with a date greater than the value | [optional] 
**lt** | **date** | Less Than - search for events with a date less than the value | [optional] 
**eq** | **date** | Equal - search for events with a date equal to the value | [optional] 
}

## Example

```python
from sailpoint.nerm.models.audit_event_created_at import AuditEventCreatedAt

audit_event_created_at = AuditEventCreatedAt(
gt=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
lt=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
eq=datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
)

```
[[Back to top]](#) 

