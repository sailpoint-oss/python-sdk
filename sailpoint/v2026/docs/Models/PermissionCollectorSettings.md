---
id: v2026-permission-collector-settings
title: PermissionCollectorSettings
pagination_label: PermissionCollectorSettings
sidebar_label: PermissionCollectorSettings
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'PermissionCollectorSettings', 'V2026PermissionCollectorSettings'] 
slug: /tools/sdk/python/v2026/models/permission-collector-settings
tags: ['SDK', 'Software Development Kit', 'PermissionCollectorSettings', 'V2026PermissionCollectorSettings']
---

# PermissionCollectorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates whether the feature or configuration is enabled. | [optional] [default to False]
**cluster_id** | **str** | The identifier of the cluster associated with this configuration, if applicable. | [optional] 
**analyze_unique_permissions** | **bool** | Indicates whether unique permissions should be analyzed for resources. | [optional] [default to False]
**calculate_effective_permissions** | **bool** | Indicates whether effective permissions should be calculated. | [optional] [default to False]
**calculate_riskiest_permissions** | **bool** | Indicates whether riskiest permissions should be calculated. | [optional] [default to False]
**effective_permissions_source** | **str** | Source for effective permissions calculation. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.permission_collector_settings import PermissionCollectorSettings

permission_collector_settings = PermissionCollectorSettings(
is_enabled=True,
cluster_id='cluster-001',
analyze_unique_permissions=True,
calculate_effective_permissions=True,
calculate_riskiest_permissions=False,
effective_permissions_source='S3'
)

```
[[Back to top]](#) 

