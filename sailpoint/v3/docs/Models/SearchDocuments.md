---
id: search-documents
title: SearchDocuments
pagination_label: SearchDocuments
sidebar_label: SearchDocuments
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SearchDocuments', 'SearchDocuments'] 
slug: /tools/sdk/python/v3/models/search-documents
tags: ['SDK', 'Software Development Kit', 'SearchDocuments', 'SearchDocuments']
---

# SearchDocuments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Access item's description. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **datetime** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the `synced` time and the time when the updated data is actually available in the search API.  | [optional] 
**enabled** | **bool** | Indicates whether the access item is currently enabled. | [optional] [default to False]
**requestable** | **bool** | Indicates whether the access item can be requested. | [optional] [default to True]
**request_comments_required** | **bool** | Indicates whether comments are required for requests to access the item. | [optional] [default to False]
**owner** | [**BaseAccessOwner**](base-access-owner) |  | [optional] 
**id** | **str** | ID of the role. | [required]
**name** | **str** | Name of the role. | [required]
**source** | [**IdentityDocumentAllOfSource**](identity-document-all-of-source) |  | [optional] 
**entitlements** | [**[]RoleDocumentAllOfEntitlements**](role-document-all-of-entitlements) | Entitlements included with the role. | [optional] 
**entitlement_count** | **int** | Number of entitlements included with the role. | [optional] 
**segments** | [**[]BaseSegment**](base-segment) | Segments with the role. | [optional] 
**segment_count** | **int** | Number of segments with the role. | [optional] 
**tags** | **[]str** | Tags that have been applied to the object. | [optional] 
**apps** | [**[]App**](app) | List of applications the identity has access to. | [optional] 
**pod** | **str** | Name of the pod. | [optional] 
**org** | **str** | Name of the tenant. | [optional] 
**type** | [**DocumentType**](document-type) |  | [optional] 
**type** | [**DocumentType**](document-type) |  | [optional] 
**version** | **str** | Version number. | [optional] 
**action** | **str** | Name of the event as it's displayed in audit reports. | [optional] 
**stage** | **str** | Activity's current stage. | [optional] 
**status** | **str** | Identity's status in SailPoint. | [optional] 
**requester** | [**ActivityIdentity**](activity-identity) |  | [optional] 
**recipient** | [**ActivityIdentity**](activity-identity) |  | [optional] 
**tracking_number** | **str** | ID of the group of events. | [optional] 
**errors** | **[]str** | Errors provided by the source while completing account actions. | [optional] 
**warnings** | **[]str** | Warnings provided by the source while completing account actions. | [optional] 
**approvals** | [**[]Approval**](approval) | Approvals performed on an item during activity. | [optional] 
**original_requests** | [**[]OriginalRequest**](original-request) | Original actions that triggered all individual source actions related to the account action. | [optional] 
**expansion_items** | [**[]ExpansionItem**](expansion-item) | Controls that translated the attribute requests into actual provisioning actions on the source. | [optional] 
**account_requests** | [**[]AccountRequest**](account-request) | Account data for each individual source action triggered by the original requests. | [optional] 
**sources** | **str** | Sources involved in the account activity. | [optional] 
**display_name** | **str** | Identity's display name. | [optional] 
**cloud_governed** | **bool** | Indicates whether the entitlement is cloud governed. | [optional] [default to False]
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**attribute** | **str** | Attribute information for the entitlement. | [optional] 
**value** | **str** | Value of the entitlement. | [optional] 
**source_schema_object_type** | **str** | Source schema object type of the entitlement. | [optional] 
**var_schema** | **str** | Schema type of the entitlement. | [optional] 
**hash** | **str** | Read-only calculated hash value of an entitlement. | [optional] 
**attributes** | **map[string]object** | Map or dictionary of key/value pairs. | [optional] 
**truncated_attributes** | **[]str** | Truncated attributes of the entitlement. | [optional] 
**contains_data_access** | **bool** | Indicates whether the entitlement contains data access. | [optional] [default to False]
**manually_updated_fields** | [**EntitlementDocumentAllOfManuallyUpdatedFields**](entitlement-document-all-of-manually-updated-fields) |  | [optional] 
**permissions** | [**[]EntitlementDocumentAllOfPermissions**](entitlement-document-all-of-permissions) |  | [optional] 
**actor** | [**EventActor**](event-actor) |  | [optional] 
**target** | [**EventTarget**](event-target) |  | [optional] 
**stack** | **str** | The event's stack. | [optional] 
**ip_address** | **str** | Target system's IP address. | [optional] 
**details** | **str** | ID of event's details. | [optional] 
**objects** | **[]str** | Objects the event is happening to. | [optional] 
**operation** | **str** | Operation, or action, performed during the event. | [optional] 
**technical_name** | **str** | Event's normalized name. This normalized name always follows the pattern of 'objects_operation_status'. | [optional] 
**first_name** | **str** | Identity's first name. | [optional] 
**last_name** | **str** | Identity's last name. | [optional] 
**email** | **str** | Identity's primary email address. | [optional] 
**phone** | **str** | Identity's phone number. | [optional] 
**inactive** | **bool** | Indicates whether the identity is inactive. | [optional] [default to False]
**protected** | **bool** | Indicates whether the identity is protected. | [optional] [default to False]
**employee_number** | **str** | Identity's employee number. | [optional] 
**manager** | [**IdentityDocumentAllOfManager**](identity-document-all-of-manager) |  | [optional] 
**is_manager** | **bool** | Indicates whether the identity is a manager of other identities. | [optional] 
**identity_profile** | [**IdentityDocumentAllOfIdentityProfile**](identity-document-all-of-identity-profile) |  | [optional] 
**disabled** | **bool** | Indicates whether the identity is disabled. | [optional] [default to False]
**locked** | **bool** | Indicates whether the identity is locked. | [optional] [default to False]
**processing_state** | **str** | Identity's processing state. | [optional] 
**processing_details** | [**ProcessingDetails**](processing-details) |  | [optional] 
**accounts** | [**[]BaseAccount**](base-account) | List of accounts associated with the identity. | [optional] 
**account_count** | **int** | Number of accounts associated with the identity. | [optional] 
**app_count** | **int** | Number of applications the identity has access to. | [optional] 
**access** | [**[]IdentityAccess**](identity-access) | List of access items assigned to the identity. | [optional] 
**access_count** | **int** | Number of access items assigned to the identity. | [optional] 
**role_count** | **int** | Number of roles assigned to the identity. | [optional] 
**access_profile_count** | **int** | Number of access profiles included with the role. | [optional] 
**owns** | [**[]Owns**](owns) | Access items the identity owns. | [optional] 
**owns_count** | **int** | Number of access items the identity owns. | [optional] 
**tags_count** | **int** | Number of tags on the identity. | [optional] 
**visible_segments** | **[]str** | List of segments that the identity is in. | [optional] 
**visible_segment_count** | **int** | Number of segments the identity is in. | [optional] 
**access_profiles** | [**[]BaseAccessProfile**](base-access-profile) | Access profiles included with the role. | [optional] 
**dimensional** | **bool** |  | [optional] [default to False]
**dimension_schema_attribute_count** | **int** | Number of dimension attributes included with the role. | [optional] 
**dimension_schema_attributes** | [**[]RoleDocumentAllOfDimensionSchemaAttributes**](role-document-all-of-dimension-schema-attributes) | Dimension attributes included with the role. | [optional] 
**dimensions** | [**[]RoleDocumentAllOfDimensions**](role-document-all-of-dimensions) |  | [optional] 
}

## Example

```python
from sailpoint.v3.models.search_documents import SearchDocuments

search_documents = SearchDocuments(
description='Admin access',
created='2018-06-25T20:22:28.104Z',
modified='2018-06-25T20:22:28.104Z',
synced='2018-06-25T20:22:33.104Z',
enabled=True,
requestable=True,
request_comments_required=False,
owner=sailpoint.v3.models.base_access_owner.BaseAccess_owner(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', 
                    email = 'cloud-support@sailpoint.com', ),
id='2c91808375d8e80a0175e1f88a575222',
name='Branch Manager Access',
source=sailpoint.v3.models.identity_document_all_of_source.IdentityDocument_allOf_source(
                    id = '2c91808b6e9e6fb8016eec1a2b6f7b5f', 
                    name = 'ODS-HR-Employees', ),
entitlements=[
                    null
                    ],
entitlement_count=3,
segments=[
                    sailpoint.v3.models.base_segment.BaseSegment(
                        id = 'b009b6e3-b56d-41d9-8735-cb532ea0b017', 
                        name = 'Test Segment', )
                    ],
segment_count=1,
tags=[TAG_1, TAG_2],
apps=[
                    null
                    ],
pod='pod01-useast1',
org='org-name',
type='identity',
type='identity',
version='v2',
action='AddEntitlement',
stage='Completed',
status='UNREGISTERED',
requester=,
recipient=,
tracking_number='63f891e0735f4cc8bf1968144a1e7440',
errors=[
                    ''
                    ],
warnings=[
                    ''
                    ],
approvals=[
                    sailpoint.v3.models.approval.Approval(
                        comments = [
                            sailpoint.v3.models.approval_comment.ApprovalComment(
                                comment = 'This request was autoapproved by our automated ETS subscriber.', 
                                commenter = 'Automated AR Approval', 
                                date = '2018-06-25T20:22:28.104Z', )
                            ], 
                        modified = '2018-06-25T20:22:28.104Z', 
                        owner = null, 
                        result = 'Finished', 
                        attribute_request = sailpoint.v3.models.attribute_request.AttributeRequest(
                            name = 'groups', 
                            op = 'Add', 
                            value = null, ), 
                        source = null, )
                    ],
original_requests=[
                    sailpoint.v3.models.original_request.OriginalRequest(
                        account_id = 'CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com', 
                        result = sailpoint.v3.models.result.Result(
                            status = 'Manual Task Created', ), 
                        attribute_requests = [
                            sailpoint.v3.models.attribute_request.AttributeRequest(
                                name = 'groups', 
                                op = 'Add', 
                                value = null, )
                            ], 
                        op = 'add', 
                        source = null, )
                    ],
expansion_items=[
                    sailpoint.v3.models.expansion_item.ExpansionItem(
                        account_id = '2c91808981f58ea601821c3e93482e6f', 
                        cause = 'Role', 
                        name = 'smartsheet-role', 
                        attribute_request = sailpoint.v3.models.attribute_request.AttributeRequest(
                            name = 'groups', 
                            op = 'Add', 
                            value = null, ), 
                        source = null, 
                        id = 'ac2887ffe0e7435a8c18c73f7ae94c7b', 
                        state = 'EXECUTING', )
                    ],
account_requests=[
                    sailpoint.v3.models.account_request.AccountRequest(
                        account_id = 'John.Doe', 
                        attribute_requests = [
                            sailpoint.v3.models.attribute_request.AttributeRequest(
                                name = 'groups', 
                                op = 'Add', 
                                value = null, )
                            ], 
                        op = 'Modify', 
                        provisioning_target = null, 
                        result = sailpoint.v3.models.account_request_result.AccountRequest_result(
                            errors = [
                                '[ConnectorError] [
  {
    "code": "unrecognized_keys",
    "keys": [
      "groups"
    ],
    "path": [],
    "message": "Unrecognized key(s) in object: 'groups'"
  }
] (requestId: 5e9d6df5-9b1b-47d9-9bf1-dc3a2893299e)'
                                ], 
                            status = 'failed', 
                            ticket_id = '', ), 
                        source = null, )
                    ],
sources='smartsheet-test, airtable-v4, IdentityNow',
display_name='Carol.Adams',
cloud_governed=False,
privileged=False,
attribute='groups',
value='1733ff75-441e-4327-9bfc-3ac445fd8cd1',
source_schema_object_type='group',
var_schema='group',
hash='c6fab95235584cca98a454a2f51e5683bc77d6a0',
attributes={country=US, firstname=Carol, cloudStatus=UNREGISTERED},
truncated_attributes=[
                    ''
                    ],
contains_data_access=True,
manually_updated_fields=sailpoint.v3.models.entitlement_document_all_of_manually_updated_fields.EntitlementDocument_allOf_manuallyUpdatedFields(
                    description = False, 
                    display_name = False, ),
permissions=[
                    sailpoint.v3.models.entitlement_document_all_of_permissions.EntitlementDocument_allOf_permissions(
                        target = 'SYS.GV_$TRANSACTION', 
                        rights = [
                            'SELECT'
                            ], )
                    ],
actor=sailpoint.v3.models.event_actor.Event_actor(
                    name = 'System', ),
target=sailpoint.v3.models.event_target.Event_target(
                    name = 'Carol.Adams', ),
stack='tpe',
ip_address='52.52.97.85',
details='73b65dfbed1842548c207432a18c84b0',
objects=[
                    'AUTHENTICATION'
                    ],
operation='ADD',
technical_name='ENTITLEMENT_ADD_PASSED',
first_name='Carol',
last_name='Adams',
email='Carol.Adams@sailpointdemo.com',
phone='+1 440-527-3672',
inactive=False,
protected=False,
employee_number='1a2a3d4e',
manager=sailpoint.v3.models.identity_document_all_of_manager.IdentityDocument_allOf_manager(
                    id = '2c9180867dfe694b017e208e27c05799', 
                    name = 'Amanda.Ross', 
                    display_name = 'Amanda.Ross', ),
is_manager=False,
identity_profile=sailpoint.v3.models.identity_document_all_of_identity_profile.IdentityDocument_allOf_identityProfile(
                    id = '3bc8ad26b8664945866b31339d1ff7d2', 
                    name = 'HR Employees', ),
disabled=False,
locked=False,
processing_state='ERROR',
processing_details=sailpoint.v3.models.processing_details.ProcessingDetails(
                    date = '2018-06-25T20:22:28.104Z', 
                    stage = 'In Process', 
                    retry_count = 0, 
                    stack_trace = '<stack trace>', 
                    message = '<message>', ),
accounts=[
                    null
                    ],
account_count=3,
app_count=2,
access=[
                    null
                    ],
access_count=5,
role_count=1,
access_profile_count=1,
owns=[
                    sailpoint.v3.models.owns.Owns(
                        sources = [
                            sailpoint.v3.models.reference.Reference(
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'John Doe', )
                            ], 
                        entitlements = [
                            sailpoint.v3.models.reference.Reference(
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'John Doe', )
                            ], 
                        access_profiles = [
                            
                            ], 
                        roles = [
                            
                            ], 
                        apps = [
                            
                            ], 
                        governance_groups = [
                            
                            ], 
                        fallback_approver = False, )
                    ],
owns_count=5,
tags_count=56,
visible_segments=[All Employees],
visible_segment_count=1,
access_profiles=[
                    sailpoint.v3.models.base_access_profile.BaseAccessProfile(
                        id = '2c91809c6faade77016fb4f0b63407ae', 
                        name = 'Admin Access', )
                    ],
dimensional=False,
dimension_schema_attribute_count=3,
dimension_schema_attributes=[
                    sailpoint.v3.models.role_document_all_of_dimension_schema_attributes.RoleDocument_allOf_dimensionSchemaAttributes(
                        derived = True, 
                        display_name = 'Department', 
                        name = 'department', )
                    ],
dimensions=[
                    sailpoint.v3.models.role_document_all_of_dimensions.RoleDocument_allOf_dimensions(
                        id = 'b3c28992ba964a40a7598978139d1ced', 
                        name = 'Manager Austin Branch', 
                        description = 'Managers located at the Austin branch', 
                        entitlements = [
                            null
                            ], 
                        access_profiles = [
                            sailpoint.v3.models.base_access_profile.BaseAccessProfile(
                                id = '2c91809c6faade77016fb4f0b63407ae', 
                                name = 'Admin Access', )
                            ], )
                    ]
)

```
[[Back to top]](#) 

