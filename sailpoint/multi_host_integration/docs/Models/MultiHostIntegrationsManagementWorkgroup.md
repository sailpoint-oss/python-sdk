---
id: multi-host-integrations-management-workgroup
title: MultiHostIntegrationsManagementWorkgroup
pagination_label: MultiHostIntegrationsManagementWorkgroup
sidebar_label: MultiHostIntegrationsManagementWorkgroup
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'MultiHostIntegrationsManagementWorkgroup', 'MultiHostIntegrationsManagementWorkgroup'] 
slug: /tools/sdk/python/multi-host-integration/models/multi-host-integrations-management-workgroup
tags: ['SDK', 'Software Development Kit', 'MultiHostIntegrationsManagementWorkgroup', 'MultiHostIntegrationsManagementWorkgroup']
---

# MultiHostIntegrationsManagementWorkgroup

Reference to management workgroup for the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'GOVERNANCE_GROUP' ] | Type of object being referenced. | [optional] 
**id** | **str** | Management workgroup ID. | [optional] 
**name** | **str** | Management workgroup's human-readable display name. | [optional] 
}

## Example

```python
from sailpoint.multi_host_integration.models.multi_host_integrations_management_workgroup import MultiHostIntegrationsManagementWorkgroup

multi_host_integrations_management_workgroup = MultiHostIntegrationsManagementWorkgroup(
type='GOVERNANCE_GROUP',
id='2c91808568c529c60168cca6f90c2222',
name='My Management Workgroup'
)

```
[[Back to top]](#) 

