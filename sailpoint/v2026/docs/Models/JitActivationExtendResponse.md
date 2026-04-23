---
id: v2026-jit-activation-extend-response
title: JitActivationExtendResponse
pagination_label: JitActivationExtendResponse
sidebar_label: JitActivationExtendResponse
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitActivationExtendResponse', 'V2026JitActivationExtendResponse'] 
slug: /tools/sdk/python/v2026/models/jit-activation-extend-response
tags: ['SDK', 'Software Development Kit', 'JitActivationExtendResponse', 'V2026JitActivationExtendResponse']
---

# JitActivationExtendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Workflow or business identifier for this activation. | [required]
**connection_id** | **str** | Entitlement connection identifier for the activation. | [required]
**activation_period_extension_mins** | **int** | Extension applied to the activation period, in minutes. | [required]
**status** | [**ActivationWorkflowStatus**](activation-workflow-status) |  | [required]
**start_time** | **datetime** | Time associated with this extend request (ISO-8601). | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_activation_extend_response import JitActivationExtendResponse

jit_activation_extend_response = JitActivationExtendResponse(
id='jit-activation-abc123',
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
activation_period_extension_mins=120,
status='PROVISIONED',
start_time='2025-10-11T21:23:15Z'
)

```
[[Back to top]](#) 

