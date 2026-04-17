---
id: audit-event-data
title: AuditEventData
pagination_label: AuditEventData
sidebar_label: AuditEventData
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AuditEventData', 'AuditEventData'] 
slug: /tools/sdk/python//models/audit-event-data
tags: ['SDK', 'Software Development Kit', 'AuditEventData', 'AuditEventData']
---

# AuditEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | The profile id associated with the event | [optional] 
**workflow_id** | **str** | The workflow id associated with the event | [optional] 
**workflow_name** | **str** | The workflow name associated with the event | [optional] 
**workflow_uid** | **str** | The workflow uid associated with the event | [optional] 
**profile_type_id** | **str** | The profile type associated with the event | [optional] 
}

## Example

```python
from sailpoint.nerm.models.audit_event_data import AuditEventData

audit_event_data = AuditEventData(
profile_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
workflow_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
workflow_name='My Workflow',
workflow_uid='my_workflow',
profile_type_id='7d8c53ca-e99d-485c-9524-ea3849e82c79'
)

```
[[Back to top]](#) 

