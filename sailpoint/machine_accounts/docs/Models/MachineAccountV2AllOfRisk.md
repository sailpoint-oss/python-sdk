---
id: machine-account-v2-all-of-risk
title: MachineAccountV2AllOfRisk
pagination_label: MachineAccountV2AllOfRisk
sidebar_label: MachineAccountV2AllOfRisk
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountV2AllOfRisk', 'MachineAccountV2AllOfRisk'] 
slug: /tools/sdk/python/machine-accounts/models/machine-account-v2-all-of-risk
tags: ['SDK', 'Software Development Kit', 'MachineAccountV2AllOfRisk', 'MachineAccountV2AllOfRisk']
---

# MachineAccountV2AllOfRisk

Risk for this machine account, set by enrichment. Null when no risk has been recorded or when risk enrichment is not enabled for the tenant. Read-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | Risk score from 0 to 100. Null when only a severity has been recorded. | [optional] 
**severity** |  **Enum** [  'UNKNOWN',    'LOW',    'MEDIUM',    'HIGH',    'CRITICAL' ] | Risk severity. | [optional] 
}

## Example

```python
from sailpoint.machine_accounts.models.machine_account_v2_all_of_risk import MachineAccountV2AllOfRisk

machine_account_v2_all_of_risk = MachineAccountV2AllOfRisk(
score=72.5,
severity='HIGH'
)

```
[[Back to top]](#) 

