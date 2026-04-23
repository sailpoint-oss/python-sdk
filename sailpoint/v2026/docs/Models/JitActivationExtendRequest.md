---
id: v2026-jit-activation-extend-request
title: JitActivationExtendRequest
pagination_label: JitActivationExtendRequest
sidebar_label: JitActivationExtendRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'JitActivationExtendRequest', 'V2026JitActivationExtendRequest'] 
slug: /tools/sdk/python/v2026/models/jit-activation-extend-request
tags: ['SDK', 'Software Development Kit', 'JitActivationExtendRequest', 'V2026JitActivationExtendRequest']
---

# JitActivationExtendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | Entitlement connection identifier for the activation to extend. | [required]
**activation_period_extension_mins** | **int** | Number of minutes to extend the activation period. | [required]
}

## Example

```python
from sailpoint.v2026.models.jit_activation_extend_request import JitActivationExtendRequest

jit_activation_extend_request = JitActivationExtendRequest(
connection_id='757fb803-9024-5861-e510-83a56e4c5bd3',
activation_period_extension_mins=120
)

```
[[Back to top]](#) 

