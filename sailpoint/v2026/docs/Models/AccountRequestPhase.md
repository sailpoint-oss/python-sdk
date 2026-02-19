---
id: v2026-account-request-phase
title: AccountRequestPhase
pagination_label: AccountRequestPhase
sidebar_label: AccountRequestPhase
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccountRequestPhase', 'V2026AccountRequestPhase'] 
slug: /tools/sdk/python/v2026/models/account-request-phase
tags: ['SDK', 'Software Development Kit', 'AccountRequestPhase', 'V2026AccountRequestPhase']
---

# AccountRequestPhase

Contains detailed information about each phase in the account request process, including its type, current state, and relevant timestamps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** |  **Enum** [  'APPROVAL_PHASE',    'PROVISIONING_PHASE' ] | Enum of account request phase type | [optional] 
**state** | [**AccountRequestPhaseState**](account-request-phase-state) |  | [optional] 
**started** | **datetime** | Start date of account request phase. | [optional] [readonly] 
**finished** | **datetime** | Finish date of account request phase. | [optional] [readonly] 
}

## Example

```python
from sailpoint.v2026.models.account_request_phase import AccountRequestPhase

account_request_phase = AccountRequestPhase(
name='APPROVAL_PHASE',
state='APPROVED',
started='2026-01-21T11:43:22.432Z',
finished='2026-01-21T11:45:22.432Z'
)

```
[[Back to top]](#) 

