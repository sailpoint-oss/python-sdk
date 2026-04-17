---
id: search200-response
title: Search200Response
pagination_label: Search200Response
sidebar_label: Search200Response
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Search200Response', 'Search200Response'] 
slug: /tools/sdk/python//models/search200-response
tags: ['SDK', 'Software Development Kit', 'Search200Response', 'Search200Response']
---

# Search200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_events** | [**[]AuditEvent**](audit-event) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.search200_response import Search200Response

search200_response = Search200Response(
audit_events=[
                    sailpoint.nerm.models.audit_event.AuditEvent(
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
                    ]
)

```
[[Back to top]](#) 

