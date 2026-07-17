---
id: tenant-configuration-details
title: TenantConfigurationDetails
pagination_label: TenantConfigurationDetails
sidebar_label: TenantConfigurationDetails
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'TenantConfigurationDetails', 'TenantConfigurationDetails'] 
slug: /tools/sdk/python/work-reassignment/models/tenant-configuration-details
tags: ['SDK', 'Software Development Kit', 'TenantConfigurationDetails', 'TenantConfigurationDetails']
---

# TenantConfigurationDetails

Details of any tenant-wide Reassignment Configurations (eg. enabled/disabled)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Flag to determine if Reassignment Configuration is enabled or disabled for a tenant.  When this flag is set to true, Reassignment Configuration is disabled. | [optional] [default to False]
}

## Example

```python
from sailpoint.work_reassignment.models.tenant_configuration_details import TenantConfigurationDetails

tenant_configuration_details = TenantConfigurationDetails(
disabled=True
)

```
[[Back to top]](#) 

