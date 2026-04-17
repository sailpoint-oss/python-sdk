---
id: search-request-audit-events
title: SearchRequestAuditEvents
pagination_label: SearchRequestAuditEvents
sidebar_label: SearchRequestAuditEvents
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SearchRequestAuditEvents', 'SearchRequestAuditEvents'] 
slug: /tools/sdk/python//models/search-request-audit-events
tags: ['SDK', 'Software Development Kit', 'SearchRequestAuditEvents', 'SearchRequestAuditEvents']
---

# SearchRequestAuditEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | How many records to skip before pulling records to return. | [optional] 
**sort_by** | **str** | A column that we are sorting these records from. | [optional] 
**limit** | **int** | The limiting count for the amount of records returned. | [optional] 
**order** |  **Enum** [  'asc',    'desc' ] | Which direction the list should be sorted by | [optional] 
**filters** | [**AuditEvent**](audit-event) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.search_request_audit_events import SearchRequestAuditEvents

search_request_audit_events = SearchRequestAuditEvents(
offset=100,
sort_by='created_at',
limit=10,
order='asc',
filters=sailpoint.nerm.models.audit_event.AuditEvent(
                    created_at = sailpoint.nerm.models.audit_event_created_at.AuditEvent_created_at(
                        gt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        lt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        eq = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ), 
                    subject_type = 'Profile', 
                    type = 'AuditableProfileCreate', 
                    subject_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', 
                    data = sailpoint.nerm.models.audit_event_data.AuditEvent_data(
                        profile_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', 
                        workflow_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', 
                        workflow_name = 'My Workflow', 
                        workflow_uid = 'my_workflow', 
                        profile_type_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', ), )
)

```
[[Back to top]](#) 

