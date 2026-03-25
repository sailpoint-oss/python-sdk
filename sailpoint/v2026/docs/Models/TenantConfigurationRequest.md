---
id: v2026-tenant-configuration-request
title: TenantConfigurationRequest
pagination_label: TenantConfigurationRequest
sidebar_label: TenantConfigurationRequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TenantConfigurationRequest', 'V2026TenantConfigurationRequest'] 
slug: /tools/sdk/python/v2026/models/tenant-configuration-request
tags: ['SDK', 'Software Development Kit', 'TenantConfigurationRequest', 'V2026TenantConfigurationRequest']
---

# TenantConfigurationRequest

Tenant-wide Reassignment Configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_details** | [**TenantConfigurationDetails**](tenant-configuration-details) |  | [optional] 
}

## Example

```python
from sailpoint.v2026.models.tenant_configuration_request import TenantConfigurationRequest

tenant_configuration_request = TenantConfigurationRequest(
config_details=sailpoint.v2026.models.tenant_configuration_details.TenantConfigurationDetails(
                    disabled = True, )
)

```
[[Back to top]](#) 

