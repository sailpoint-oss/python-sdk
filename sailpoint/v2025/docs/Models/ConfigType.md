---
id: v2025-config-type
title: ConfigType
pagination_label: ConfigType
sidebar_label: ConfigType
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'ConfigType', 'V2025ConfigType'] 
slug: /tools/sdk/python/v2025/models/config-type
tags: ['SDK', 'Software Development Kit', 'ConfigType', 'V2025ConfigType']
---

# ConfigType

Type of Reassignment Configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] 
**internal_name** | [**ConfigTypeEnumCamel**](config-type-enum-camel) |  | [optional] 
**internal_name_camel** | [**ConfigTypeEnum**](config-type-enum) |  | [optional] 
**display_name** | **str** | Human readable display name of the type to be shown on UI | [optional] 
**description** | **str** | Description of the type of work to be reassigned, displayed by the UI. | [optional] 
}

## Example

```python
from sailpoint.v2025.models.config_type import ConfigType

config_type = ConfigType(
priority=1,
internal_name='accessRequests',
internal_name_camel='ACCESS_REQUESTS',
display_name='Access Requests',
description='Reassign Access Request Work Items for an identity'
)

```
[[Back to top]](#) 

