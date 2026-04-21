---
id: v2026-jit-access-operation-request
title: JitAccessOperationRequest
pagination_label: JitAccessOperationRequest
sidebar_label: JitAccessOperationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitAccessOperationRequest', 'V2026JitAccessOperationRequest'] 
slug: /tools/sdk/python/v2026/models/jit-access-operation-request
tags: ['SDK', 'Software Development Kit', 'JitAccessOperationRequest', 'V2026JitAccessOperationRequest']
---

# JitAccessOperationRequest

A single replace operation applied to JIT activation configuration. Only **replace** is supported. **path** must be one of the allowed JSON Pointer-style paths. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** |  **Enum** [  'replace' ] | Operation type. Defaults to `replace` if omitted. | [optional] [default to 'replace']
**path** |  **Enum** [  '/entitlementIds',    '/maxActivationPeriodMins',    '/maxActivationPeriodExtensionMins',    '/defaultMaxActivationPeriodMins',    '/defaultMaxActivationPeriodExtensionMins',    '/notificationRecipients',    '/notificationTemplate',    '/applyToFutureAssignments' ] | Path to replace. Only the following JSON Pointer-style paths are supported.  | [required]
**value** | [**JitAccessOperationRequestValue**](jit-access-operation-request-value) |  | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_access_operation_request import JitAccessOperationRequest

jit_access_operation_request = JitAccessOperationRequest(
op='replace',
path='/maxActivationPeriodMins',
value=60
)

```
[[Back to top]](#) 

