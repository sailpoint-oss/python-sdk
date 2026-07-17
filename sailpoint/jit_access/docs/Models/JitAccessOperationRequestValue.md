---
id: jit-access-operation-request-value
title: JitAccessOperationRequestValue
pagination_label: JitAccessOperationRequestValue
sidebar_label: JitAccessOperationRequestValue
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitAccessOperationRequestValue', 'JitAccessOperationRequestValue'] 
slug: /tools/sdk/python/jit-access/models/jit-access-operation-request-value
tags: ['SDK', 'Software Development Kit', 'JitAccessOperationRequestValue', 'JitAccessOperationRequestValue']
---

# JitAccessOperationRequestValue

New value. Type depends on **path**: arrays of strings for `/entitlementIds` and `/notificationRecipients`, integer for `*Mins` paths, string for `/notificationTemplate`, boolean for `/applyToFutureAssignments`. Use `null` when clearing nullable fields (for example `/notificationTemplate` or `*Mins` paths). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
}

## Example

```python
from sailpoint.jit_access.models.jit_access_operation_request_value import JitAccessOperationRequestValue

jit_access_operation_request_value = JitAccessOperationRequestValue(
)

```
[[Back to top]](#) 

