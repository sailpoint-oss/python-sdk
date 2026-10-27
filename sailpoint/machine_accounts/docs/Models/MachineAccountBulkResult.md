---
id: machine-account-bulk-result
title: MachineAccountBulkResult
pagination_label: MachineAccountBulkResult
sidebar_label: MachineAccountBulkResult
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MachineAccountBulkResult', 'MachineAccountBulkResult'] 
slug: /tools/sdk/python/machine-accounts/models/machine-account-bulk-result
tags: ['SDK', 'Software Development Kit', 'MachineAccountBulkResult', 'MachineAccountBulkResult']
---

# MachineAccountBulkResult

The outcome of a bulk operation for one machine account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the machine account this result applies to. | [optional] 
**status** | **int** | HTTP-style status code for this machine account. `200` means the operation succeeded or was queued. Other values, such as `400`, `404` or `500`, describe why it failed. | [optional] 
**message** | **str** | A message that describes the outcome for this machine account. | [optional] 
}

## Example

```python
from sailpoint.machine_accounts.models.machine_account_bulk_result import MachineAccountBulkResult

machine_account_bulk_result = MachineAccountBulkResult(
id='ef38f94347e94562b5bb8424a56397d8',
status=200,
message='Success'
)

```
[[Back to top]](#) 

