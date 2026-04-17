---
id: search-request
title: SearchRequest
pagination_label: SearchRequest
sidebar_label: SearchRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SearchRequest', 'SearchRequest'] 
slug: /tools/sdk/python//models/search-request
tags: ['SDK', 'Software Development Kit', 'SearchRequest', 'SearchRequest']
---

# SearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_events** | [**SearchRequestAuditEvents**](search-request-audit-events) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.search_request import SearchRequest

search_request = SearchRequest(
audit_events=sailpoint.nerm.models.search_request_audit_events.search_request_audit_events(
                    offset = 100, 
                    sort_by = 'created_at', 
                    limit = 10, 
                    order = 'asc', 
                    filters = sailpoint.nerm.models.audit_event.AuditEvent(
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
                            profile_type_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', ), ), )
)

```
[[Back to top]](#) 

