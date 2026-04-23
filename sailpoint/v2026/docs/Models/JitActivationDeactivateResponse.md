---
id: v2026-jit-activation-deactivate-response
title: JitActivationDeactivateResponse
pagination_label: JitActivationDeactivateResponse
sidebar_label: JitActivationDeactivateResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitActivationDeactivateResponse', 'V2026JitActivationDeactivateResponse'] 
slug: /tools/sdk/python/v2026/models/jit-activation-deactivate-response
tags: ['SDK', 'Software Development Kit', 'JitActivationDeactivateResponse', 'V2026JitActivationDeactivateResponse']
---

# JitActivationDeactivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Workflow or business identifier for this activation. | [required]
**connection_id** | **str** | Entitlement connection identifier for the activation. | [required]
**status** | [**ActivationWorkflowStatus**](activation-workflow-status) |  | [required]
**start_time** | **datetime** | Time associated with this deactivation request (ISO-8601). | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_activation_deactivate_response import JitActivationDeactivateResponse

jit_activation_deactivate_response = JitActivationDeactivateResponse(
id='jit-activation-abc123',
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
status='PROVISIONED',
start_time='2025-10-11T21:23:15Z'
)

```
[[Back to top]](#) 

