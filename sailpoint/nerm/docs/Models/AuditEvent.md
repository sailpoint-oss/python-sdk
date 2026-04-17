---
id: audit-event
title: AuditEvent
pagination_label: AuditEvent
sidebar_label: AuditEvent
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AuditEvent', 'AuditEvent'] 
slug: /tools/sdk/python//models/audit-event
tags: ['SDK', 'Software Development Kit', 'AuditEvent', 'AuditEvent']
---

# AuditEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | [**AuditEventCreatedAt**](audit-event-created-at) |  | [optional] 
**subject_type** |  **Enum** [  'Profile',    'WorkflowSession',    'Email',    'FormAttributeForm',    'FormAttribute',    'Form',    'IdentityProofingResult',    'IdproxyPermission',    'NeAttributeOption',    'NeAttribute',    'Notification',    'WorkflowPage',    'ProfilePage',    'Permission',    'PortalRegistrationWorkflow',    'Portal',    'ProfileTypeRole',    'ProfileType',    'RoleProfile',    'NeprofileRole',    'NeaccessRole',    'IdproxyRole',    'SecurityQuestion',    'UserManager',    'UserProfile',    'UserRole',    'User',    'Validation',    'VerificationEmail',    'WorkflowAction',    'CreateWorkflow',    'UpdateWorkflow',    'AutomatedWorkflow',    'BatchWorkflow',    'ExpirationWorkflow',    'InvitationWorkflow',    'LoginWorkflow',    'PasswordResetWorkflow',    'RegistrationWorkflow',    'Get',    'Post',    'Patch',    'Delete',    'ApprovalAction',    'AutomatedUser',    'DelegateUser',    'NeaccessUser',    'NeprofileUser',    'Page',    'Role',    'SamlConfiguration',    'SchemaMapping',    'SchemaMappingField',    'Workflow' ] | Categorization of audit event. | [optional] 
**type** |  **Enum** [  'AuditableProfileCreate',    'AuditableProfileUpdate',    'AuditableProfileDestroy',    'AuditableBulkProfileUpdate',    'AuditableProfileContributorAdd',    'AuditableProfileContributorRemove',    'AuditableProfileContributorRoleAdd',    'AuditableProfileContributorRoleRemove',    'AuditableProfileOwnerUpdate',    'AuditableProfileWorkflowEvent',    'AuditableWorkflowActionSkippedEvent',    'AuditableWorkflowApprovedEvent',    'AuditableWorkflowApprovedEvent',    'AuditableWorkflowAssignedEvent',    'AuditableWorkflowAutoAssignedEvent',    'AuditableWorkflowBatchCompleteEvent',    'AuditableWorkflowClosedEvent',    'AuditableWorkflowDuplicateCheckStartEvent',    'AuditableWorkflowDuplicateResolutionEvent',    'AuditableWorkflowFailedEvent',    'AuditableWorkflowIdentityProofedEvent',    'AuditableWorkflowInvitationSentEvent',    'AuditableWorkflowLdapProvidedEvent',    'AuditableWorkflowNotificationSentEvent',    'AuditableWorkflowPendingApprovalEvent',    'AuditableWorkflowPendingAssignmentEvent',    'AuditableWorkflowPendingFulfillmentEvent',    'AuditableWorkflowFulfilledEvent',    'AuditableWorkflowPendingIdentityProofEvent',    'AuditableWorkflowPendingLdapEvent',    'AuditableWorkflowPendingRequestEvent',    'AuditableWorkflowPendingReviewEvent',    'AuditableWorkflowProfileCreatedEvent',    'AuditableWorkflowProfileSelectEvent',    'AuditableWorkflowProfileUpdatedEvent',    'AuditableWorkflowRejectedEvent',    'AuditableWorkflowRequestMadeEvent',    'AuditableWorkflowRestApiEvent',    'AuditableWorkflowReviewedEvent',    'AuditableWorkflowRunningWorkflowEvent',    'AuditableWorkflowSoapApiEvent',    'AuditableWorkflowStatusChangedEvent',    'AuditableWorkflowStoredProcedureEvent',    'AuditableWorkflowUnassignEvent',    'AuditableWorkflowWaitingForWorkflowEvent',    'AuditableWorkflowWorkflowChangedEvent',    'ActiveRecordCreate',    'ActiveRecordUpdate',    'ActiveRecordDestroy',    'AuditableApiEvent' ] | The type of audit event | [optional] 
**subject_id** | **str** | Identifier of the subject | [optional] 
**data** | [**AuditEventData**](audit-event-data) |  | [optional] 
}

## Example

```python
from sailpoint.nerm.models.audit_event import AuditEvent

audit_event = AuditEvent(
created_at=sailpoint.nerm.models.audit_event_created_at.AuditEvent_created_at(
                    gt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    lt = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    eq = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
subject_type='Profile',
type='AuditableProfileCreate',
subject_id='7d8c53ca-e99d-485c-9524-ea3849e82c79',
data=sailpoint.nerm.models.audit_event_data.AuditEvent_data(
                    profile_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', 
                    workflow_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', 
                    workflow_name = 'My Workflow', 
                    workflow_uid = 'my_workflow', 
                    profile_type_id = '7d8c53ca-e99d-485c-9524-ea3849e82c79', )
)

```
[[Back to top]](#) 

