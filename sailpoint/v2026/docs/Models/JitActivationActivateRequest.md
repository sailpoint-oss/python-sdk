---
id: v2026-jit-activation-activate-request
title: JitActivationActivateRequest
pagination_label: JitActivationActivateRequest
sidebar_label: JitActivationActivateRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitActivationActivateRequest', 'V2026JitActivationActivateRequest'] 
slug: /tools/sdk/python/v2026/models/jit-activation-activate-request
tags: ['SDK', 'Software Development Kit', 'JitActivationActivateRequest', 'V2026JitActivationActivateRequest']
---

# JitActivationActivateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Entitlement connection identifier for the activation. | [required]
**activation_period_mins** | **int** | Requested activation duration in minutes. | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_activation_activate_request import JitActivationActivateRequest

jit_activation_activate_request = JitActivationActivateRequest(
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
activation_period_mins=120
)

```
[[Back to top]](#) 

