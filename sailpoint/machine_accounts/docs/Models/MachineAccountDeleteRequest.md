---
id: machine-account-delete-request
title: MachineAccountDeleteRequest
pagination_label: MachineAccountDeleteRequest
sidebar_label: MachineAccountDeleteRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountDeleteRequest', 'MachineAccountDeleteRequest'] 
slug: /tools/sdk/python/machine-accounts/models/machine-account-delete-request
tags: ['SDK', 'Software Development Kit', 'MachineAccountDeleteRequest', 'MachineAccountDeleteRequest']
---

# MachineAccountDeleteRequest

Details for a request to delete a machine account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Comments about the deletion request. Depending on the tenant's account deletion approval settings, comments can be required. | [optional] 
}

## Example

```python
from sailpoint.machine_accounts.models.machine_account_delete_request import MachineAccountDeleteRequest

machine_account_delete_request = MachineAccountDeleteRequest(
comments='This machine account is no longer used.'
)

```
[[Back to top]](#) 

