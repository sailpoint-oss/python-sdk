---
id: intelidentityaggregate
title: Intelidentityaggregate
pagination_label: Intelidentityaggregate
sidebar_label: Intelidentityaggregate
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentityaggregate', 'Intelidentityaggregate'] 
slug: /tools/sdk/python/intelligence/models/intelidentityaggregate
tags: ['SDK', 'Software Development Kit', 'Intelidentityaggregate', 'Intelidentityaggregate']
---

# Intelidentityaggregate

Flat identity response with identity attributes hoisted to the top level. The accounts, privilegedAccess, and accessHistory slices are always present. The outliers slice is omitted when the tenant lacks the IDA-outliers license. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity Security Cloud identifier for this identity. | [required]
**type** |  **Enum** [  'HUMAN' ] | Identity type for the matched record. | [required]
**display_name** | **str** | Preferred display name for the identity across administrative experiences. | [optional] 
**description** | **str** | Optional free-text description assigned to the identity profile when present. | [optional] 
**subtype** |  **Enum** [  'Employee',    'Non Employee',    'Cannot Determine' ] | NERM classification for the identity. | [optional] 
**owners** | **str** | Serialized owner reference information when populated by upstream identity services. | [optional] 
**attributes** | **map[string]object** | Arbitrary SCIM-style attribute bag returned for the identity context view. | [optional] 
**created** | **datetime** | Timestamp when the identity record was created in Identity Security Cloud. | [optional] 
**modified** | **datetime** | Timestamp when the identity record was last modified in Identity Security Cloud. | [optional] 
**alias** | **str** | Primary login or account alias for the identity. | [optional] 
**email** | **str** | Primary business email address for the identity. | [optional] 
**identity_status** | **str** | Current identity lifecycle status label from Identity Security Cloud. | [optional] 
**is_manager** | **bool** | True when the identity is flagged as a people manager in the organization. | [required]
**accounts** | [**Intelaccountsslice**](intelaccountsslice) | First page of accounts for the identity. | [required]
**privileged_access** | [**Intelprivilegedaccessslice**](intelprivilegedaccessslice) | Full privileged access result for the identity. | [required]
**outliers** | [**Inteloutliersslice**](inteloutliersslice) | Rare access slice; omitted when the tenant lacks the IDA-outliers license. | [optional] 
**access_history** | [**Intelaccesshistory**](intelaccesshistory) | Access-history split into access items and certifications sub-slices. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelidentityaggregate import Intelidentityaggregate

intelidentityaggregate = Intelidentityaggregate(
id='ef38f94347e94562b5bb8424a56397d8',
type='HUMAN',
display_name='Example User',
description='Example description.',
subtype='Employee',
owners='governance-group-001',
attributes={"department":"Engineering","region":"US"},
created='2026-05-12T08:00Z',
modified='2026-05-12T09:15:30Z',
alias='example.user',
email='user@example.com',
identity_status='ACTIVE',
is_manager=False,
accounts=sailpoint.intelligence.models.intelaccountsslice.intelaccountsslice(
                    items = [
                        sailpoint.intelligence.models.intelaccessaccountwire.intelaccessaccountwire(
                            id = '2c91808874ff91550175097daaec161c', 
                            name = 'jdoe', 
                            source = sailpoint.intelligence.models.source.source(), 
                            disabled = False, 
                            locked = False, 
                            authoritative = True, 
                            system_account = False, 
                            is_machine = False, 
                            manually_correlated = False, 
                            native_identity = 'CN=jdoe,OU=Users,DC=example,DC=com', 
                            created = '2023-11-01T10:00Z', 
                            modified = '2024-02-15T16:20Z', )
                        ], 
                    next = 'https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/accounts?limit=10&offset=10', ),
privileged_access=sailpoint.intelligence.models.intelprivilegedaccessslice.intelprivilegedaccessslice(
                    items = [
                        sailpoint.intelligence.models.intelprivilegedaccessitemwire.intelprivilegedaccessitemwire(
                            privileged = True, 
                            id = 'ent-1', 
                            type = 'entitlement', 
                            display_name = 'Example_Admin_Access', 
                            name = 'Example_Admin_Access', 
                            source = sailpoint.intelligence.models.intelprivilegedaccessitemwire_source.intelprivilegedaccessitemwire_source(
                                name = 'Example HR Source', 
                                id = 'src-2', ), 
                            attribute = 'EXAMPLE_PERMISSION_GROUPS', 
                            value = 'Example_Admin_Access', )
                        ], ),
outliers=sailpoint.intelligence.models.inteloutliersslice.inteloutliersslice(
                    rare_access = null, ),
access_history=sailpoint.intelligence.models.intelaccesshistory.intelaccesshistory(
                    access_items = sailpoint.intelligence.models.access_items.accessItems(), 
                    certifications = sailpoint.intelligence.models.certifications.certifications(), )
)

```
[[Back to top]](#) 

