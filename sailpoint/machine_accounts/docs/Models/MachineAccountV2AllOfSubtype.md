---
id: machine-account-v2-all-of-subtype
title: MachineAccountV2AllOfSubtype
pagination_label: MachineAccountV2AllOfSubtype
sidebar_label: MachineAccountV2AllOfSubtype
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountV2AllOfSubtype', 'MachineAccountV2AllOfSubtype'] 
slug: /tools/sdk/python/machine-accounts/models/machine-account-v2-all-of-subtype
tags: ['SDK', 'Software Development Kit', 'MachineAccountV2AllOfSubtype', 'MachineAccountV2AllOfSubtype']
---

# MachineAccountV2AllOfSubtype

The machine account subtype assigned to this machine account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the subtype. | [optional] 
**technical_name** | **str** | The technical name of the subtype. | [optional] 
**display_name** | **str** | The display name of the subtype. | [optional] 
}

## Example

```python
from sailpoint.machine_accounts.models.machine_account_v2_all_of_subtype import MachineAccountV2AllOfSubtype

machine_account_v2_all_of_subtype = MachineAccountV2AllOfSubtype(
id='43bdd144-4b17-4fce-a744-17c7fd3e717b',
technical_name='serviceAccount',
display_name='Service Account'
)

```
[[Back to top]](#) 

