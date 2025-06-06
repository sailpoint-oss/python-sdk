---
id: v2024-complete-invocation
title: CompleteInvocation
pagination_label: CompleteInvocation
sidebar_label: CompleteInvocation
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'CompleteInvocation', 'V2024CompleteInvocation'] 
slug: /tools/sdk/python/v2024/models/complete-invocation
tags: ['SDK', 'Software Development Kit', 'CompleteInvocation', 'V2024CompleteInvocation']
---

# CompleteInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Unique invocation secret that was generated when the invocation was created. Required to authenticate to the endpoint. | [required]
**error** | **str** | The error message to indicate a failed invocation or error if any. | [optional] 
**output** | **object** | Trigger output to complete the invocation. Its schema is defined in the trigger definition. | [required]
}

## Example

```python
from sailpoint.v2024.models.complete_invocation import CompleteInvocation

complete_invocation = CompleteInvocation(
secret='0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
error='Access request is denied.',
output={approved=false}
)

```
[[Back to top]](#) 

