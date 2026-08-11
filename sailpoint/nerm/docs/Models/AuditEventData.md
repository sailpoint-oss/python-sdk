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
**workflow_version_id** | **str** | The workflow version a change belongs to. Can be used for both Workflow configurations and Workflow Session events. | [optional] 
**version** | **str** | The workflow version SHA. | [optional] 
**step_id** | **str** | The id of the workflow action or condition the step event refers to. | [optional] 
**step_label** | **str** | The name associated to an action configuration. | [optional] 
**source** |  **Enum** [  'ui',    'import',    'fork',    'cleanup_worker',    'delete_worker' ] | What triggered the versioning change. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.audit_event_data import AuditEventData

audit_event_data = AuditEventData(
profile_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
workflow_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
workflow_name='My Workflow',
workflow_uid='my_workflow',
profile_type_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
workflow_version_id='e309339f-551f-48ab-b4f6-58d93123911f',
version='aadf95e45846365fa4b4c60f02c76ecffe718ee5',
step_id='2f4b24c6-d420-4eee-b860-5ad24c743185',
step_label='RequestAction',
source='ui'
)

```
[[Back to top]](#) 

