---
id: v2026-intel-identity-response
title: IntelIdentityResponse
pagination_label: IntelIdentityResponse
sidebar_label: IntelIdentityResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityResponse', 'V2026IntelIdentityResponse'] 
slug: /tools/sdk/python/v2026/models/intel-identity-response
tags: ['SDK', 'Software Development Kit', 'IntelIdentityResponse', 'V2026IntelIdentityResponse']
---

# IntelIdentityResponse

HUMAN responses include human, top-level subtype (NERM classification: Employee, Non Employee, or Cannot Determine), and _links (access, risk, and accessHistory). MACHINE responses include machine and top-level subtype (connector subtype string); _links is omitted. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identity Security Cloud identifier for this identity. | [required]
**type** |  **Enum** [  'HUMAN',    'MACHINE' ] | Discriminator indicating whether this identity is human or machine backed. | [required]
**display_name** | **str** | Preferred display name for the identity across administrative experiences. | [optional] 
**description** | **str** | Optional free-text description assigned to the identity profile when present. | [optional] 
**subtype** | **str** | For HUMAN identities, NERM classification (Employee, Non Employee, or Cannot Determine). For MACHINE identities, connector subtype string from the authoritative source.  | [optional] 
**owners** | **str** | Serialized owner reference information when populated by upstream identity services. | [optional] 
**attributes** | **map[string]object** | Arbitrary SCIM-style attribute bag returned for the identity context view. | [optional] 
**timestamps** | [**IntelIdentityTimestamps**](intel-identity-timestamps) | Created and modified timestamps for the identity record in Identity Security Cloud. | [required]
**human** | [**IntelHuman**](intel-human) | Human identity extension payload when type is HUMAN. | [optional] 
**machine** | [**IntelMachine**](intel-machine) | Machine identity extension payload when type is MACHINE. | [optional] 
**links** | [**IntelIdentityLinks**](intel-identity-links) | Hyperlinks to related Intelligence Package sub-resources; present for HUMAN only. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_identity_response import IntelIdentityResponse

intel_identity_response = IntelIdentityResponse(
id='ef38f94347e94562b5bb8424a56397d8',
type='HUMAN',
display_name='Jane Example',
description='Contractor identity for example project work.',
subtype='Employee',
owners='governance-group-001',
attributes={department=Engineering, region=US},
timestamps=sailpoint.v2026.models.intel_identity_timestamps.IntelIdentityTimestamps(
                    created_at = '2024-01-15T10:30Z', 
                    modified_at = '2024-06-20T14:45Z', ),
human=sailpoint.v2026.models.intel_human.IntelHuman(
                    alias = 'jdoe', 
                    email = 'john.doe@example.com', 
                    identity_status = 'Active', 
                    lifecycle_state = 'contractor', 
                    processing_state = 'pending', 
                    is_protected = False, 
                    manager = 'ef38f94347e94562b5bb8424a56397d9', 
                    manager_id = 'ef38f94347e94562b5bb8424a56397d9', 
                    manager_name = 'Alex Manager', 
                    is_manager = True, 
                    last_refresh_at = '2024-05-01T08:00Z', ),
machine=sailpoint.v2026.models.intel_machine.IntelMachine(
                    business_application = 'Payroll Bot', 
                    native_identity = 'example-agent-1', 
                    uuid = '3fa85f64-5717-4562-b3fc-2c963f66afa6', 
                    source_id = '8433902684054f09ae024c06cf5091c1', 
                    source = sailpoint.v2026.models.source.source(), 
                    dataset_id = 'dataset-001', 
                    exists_on_source = True, 
                    manually_created = False, 
                    manually_edited = False, 
                    owners = {}, 
                    user_entitlements = [
                        {}
                        ], ),
links=sailpoint.v2026.models.intel_identity_links.IntelIdentityLinks(
                    access = {href=/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access}, 
                    risk = {href=/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/risk}, 
                    access_history = {href=/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access-history}, )
)

```
[[Back to top]](#) 

