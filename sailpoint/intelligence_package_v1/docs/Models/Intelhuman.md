---
id: intelhuman
title: Intelhuman
pagination_label: Intelhuman
sidebar_label: Intelhuman
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelhuman', 'Intelhuman'] 
slug: /tools/sdk/python/v1/models/intelhuman
tags: ['SDK', 'Software Development Kit', 'Intelhuman', 'Intelhuman']
---

# Intelhuman


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Primary login or account alias for the human identity. | [required]
**email** | **str** | Primary business email address for the human identity. | [required]
**identity_status** | **str** | Current identity lifecycle status label from Identity Security Cloud. | [required]
**lifecycle_state** | **str** | Lifecycle state name assigned through provisioning policy when present. | [optional] 
**processing_state** | **str** | Processing state for outstanding identity change operations when present. | [optional] 
**is_protected** | **bool** | True when the identity is marked protected from automated changes. | [required]
**manager** | **str** | Legacy manager identity identifier or display reference when assigned. | [optional] 
**manager_id** | **str** | Manager identity identifier when correlated in Identity Security Cloud. | [optional] 
**manager_name** | **str** | Manager display name when available from identity services. | [optional] 
**is_manager** | **bool** | True when the identity is flagged as a people manager in the organization. | [required]
**last_refresh_at** | **datetime** | Timestamp of the last successful identity refresh from sources when known. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelhuman import Intelhuman

intelhuman = Intelhuman(
alias='jdoe',
email='john.doe@example.com',
identity_status='Active',
lifecycle_state='contractor',
processing_state='pending',
is_protected=False,
manager='ef38f94347e94562b5bb8424a56397d9',
manager_id='ef38f94347e94562b5bb8424a56397d9',
manager_name='Alex Manager',
is_manager=True,
last_refresh_at='2024-05-01T08:00Z'
)

```
[[Back to top]](#) 

