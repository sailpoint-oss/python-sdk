---
id: v2026-start-invocation-input
title: StartInvocationInput
pagination_label: StartInvocationInput
sidebar_label: StartInvocationInput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'StartInvocationInput', 'V2026StartInvocationInput'] 
slug: /tools/sdk/python/v2026/models/start-invocation-input
tags: ['SDK', 'Software Development Kit', 'StartInvocationInput', 'V2026StartInvocationInput']
---

# StartInvocationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** | Trigger ID | [optional] 
**input** | **object** | Trigger input payload. Its schema is defined in the trigger definition. | [optional] 
**content_json** | **object** | JSON map of invocation metadata | [optional] 
}

## Example

```python
from sailpoint.v2026.models.start_invocation_input import StartInvocationInput

start_invocation_input = StartInvocationInput(
trigger_id='idn:access-requested',
input={identityId=201327fda1c44704ac01181e963d463c},
content_json={workflowId=1234}
)

```
[[Back to top]](#) 

