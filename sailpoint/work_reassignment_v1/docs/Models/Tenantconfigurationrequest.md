---
id: tenantconfigurationrequest
title: Tenantconfigurationrequest
pagination_label: Tenantconfigurationrequest
sidebar_label: Tenantconfigurationrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Tenantconfigurationrequest', 'Tenantconfigurationrequest'] 
slug: /tools/sdk/python/v1/models/tenantconfigurationrequest
tags: ['SDK', 'Software Development Kit', 'Tenantconfigurationrequest', 'Tenantconfigurationrequest']
---

# Tenantconfigurationrequest

Tenant-wide Reassignment Configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_details** | [**Tenantconfigurationdetails**](tenantconfigurationdetails) |  | [optional] 
}

## Example

```python
from sailpoint.work_reassignment_v1.models.tenantconfigurationrequest import Tenantconfigurationrequest

tenantconfigurationrequest = Tenantconfigurationrequest(
config_details=sailpoint.work_reassignment_v1.models.tenantconfigurationdetails.tenantconfigurationdetails(
                    disabled = True, )
)

```
[[Back to top]](#) 

