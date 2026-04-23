---
id: v2025-role-propagation-config-input
title: RolePropagationConfigInput
pagination_label: RolePropagationConfigInput
sidebar_label: RolePropagationConfigInput
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'RolePropagationConfigInput', 'V2025RolePropagationConfigInput'] 
slug: /tools/sdk/python/v2025/models/role-propagation-config-input
tags: ['SDK', 'Software Development Kit', 'RolePropagationConfigInput', 'V2025RolePropagationConfigInput']
---

# RolePropagationConfigInput

Role Change Propagation Config Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if the Role Change Propagation process should be enabled for the tenant | [optional] [default to False]
}

## Example

```python
from sailpoint.v2025.models.role_propagation_config_input import RolePropagationConfigInput

role_propagation_config_input = RolePropagationConfigInput(
enabled=True
)

```
[[Back to top]](#) 

