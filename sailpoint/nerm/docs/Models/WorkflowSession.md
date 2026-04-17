---
id: workflow-session
title: WorkflowSession
pagination_label: WorkflowSession
sidebar_label: WorkflowSession
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'WorkflowSession', 'WorkflowSession'] 
slug: /tools/sdk/python//models/workflow-session
tags: ['SDK', 'Software Development Kit', 'WorkflowSession', 'WorkflowSession']
---

# WorkflowSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The objects ID. | [optional] [readonly] 
**uid** | **str** | The objects UID. | [optional] [readonly] 
**workflow_id** | **str** | The workflow id. | [optional] 
**requester_id** | **str** | The requester's id. | [optional] 
**requester_type** |  **Enum** [  'User',    'NeprofileUser',    'NeaccessUser' ] | The requester type. | [optional] 
**profile_id** | **str** | The profile this workflow session will be working with. Only Applicable for Update workflows | [optional] 
**profile_ids** | **[]str** | The profiles this workflow session will be working with. Only Applicable for Batch workflows | [optional] 
**status** |  **Enum** [  'api_request_sent',    'approved',    'assigned',    'attempting_to_start_workflow',    'AUTH-STATUS1',    'AUTH-STATUS2',    'AUTH-STATUS3',    'AUTH-STATUS4',    'AUTH-STATUS5',    'AUTH-STATUS6',    'AUTH-STATUS7',    'AUTH-STATUS8',    'AUTH-STATUS9',    'auto_assigned',    'batch_completed',    'checking_for_duplicates',    'closed',    'completed',    'courion_add',    'courion_extend',    'courion_terminate',    'courion_update',    'duplicates_resolved',    'failed',    'fulfilled',    'invitation_sent',    'ldap_provided',    'new',    'non_employee_created',    'non_employee_updated',    'notified',    'pending_approval',    'pending_assignment',    'pending_courion_add',    'pending_courion_extend',    'pending_courion_terminate',    'pending_courion_update',    'pending_creation',    'pending_fulfillment',    'pending_ldap',    'pending_notification',    'pending_profile_select',    'pending_request',    'pending_review',    'pending_status_change',    'pending_stored_procedure',    'pending_trigger',    'pending_update',    'processing',    'profile_check_complete',    'profiles_selected',    'rejected',    'requested',    'reviewed',    'soap_request_sent',    'started_workflow',    'status_changed',    'stored_procedure',    'un_assigned',    'waiting_on_workflow',    'workflow_changed' ] | The status of the workflow session. | [optional] 
**attributes** | **map[string]str** | The attributes asscoiated with the workflow session. | [optional] 
}

## Example

```python
from sailpoint.nerm.models.workflow_session import WorkflowSession

workflow_session = WorkflowSession(
id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
uid='wsUid',
workflow_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
requester_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
requester_type='User',
profile_id='33f072dd-13b4-41e1-8ea0-16f2a59b57c8',
profile_ids=59ed1cb6-9977-4965-9bfe-f2bcc242523e, 89ed1cb6-9977-4965-9bfe-f2bcc242523e,
status='completed',
attributes={text_attribute_uid=static text, date_attribute_uid=01/15/2020, profile_select_attribute_uid=Profile Name, profile_search_attribute_uid=Profile Name, multiple_profile_search_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, multiple_profile_select_attribute_uid=Profile Name,Second Profile Name,Third Profile Name, contributor_select_attribute_uid=User Name (user_email@test.com), contributor_search_attribute_uid=User Name (user_email@test.com), multiple_contributor_search_attribute_uid=User Name (user_email@test.com),Second User Name (user_email@test.com),Third User Name (user_email@test.com), owner_select_attribute_uid=User Name (user_email@test.com), owner_search_attribute_uid=User Name (user_email@test.com), dropdown_attribute_uid=yes, no, tags_attribute_uid=yes, no, checkbox_attribute_uid=yes, no, text_area_uid=static text, radio_attribute_uid=yes, no}
)

```
[[Back to top]](#) 

