---
id: v2026-jit-activation-activate-response
title: JitActivationActivateResponse
pagination_label: JitActivationActivateResponse
sidebar_label: JitActivationActivateResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitActivationActivateResponse', 'V2026JitActivationActivateResponse'] 
slug: /tools/sdk/python/v2026/models/jit-activation-activate-response
tags: ['SDK', 'Software Development Kit', 'JitActivationActivateResponse', 'V2026JitActivationActivateResponse']
---

# JitActivationActivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Workflow or business identifier for this activation. | [required]
**connection_id** | **str** | Entitlement connection identifier for the activation. | [required]
**activation_period_mins** | **int** | Activation duration in minutes for this workflow. | [required]
**status** | [**ActivationWorkflowStatus**](activation-workflow-status) |  | [required]
**start_time** | **datetime** | Time when the activation workflow was started (ISO-8601). | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_activation_activate_response import JitActivationActivateResponse

jit_activation_activate_response = JitActivationActivateResponse(
id='jit-activation-abc123',
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
activation_period_mins=120,
status='PROVISIONED',
start_time='2025-10-11T21:23:15Z'
)

```
[[Back to top]](#) 

