---
id: v2026-access-apps-owner
title: AccessAppsOwner
pagination_label: AccessAppsOwner
sidebar_label: AccessAppsOwner
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AccessAppsOwner', 'V2026AccessAppsOwner'] 
slug: /tools/sdk/python/v2026/models/access-apps-owner
tags: ['SDK', 'Software Development Kit', 'AccessAppsOwner', 'V2026AccessAppsOwner']
---

# AccessAppsOwner

Owner's identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'IDENTITY' ] | Owner's DTO type. | [optional] 
**id** | **str** | Owner's identity ID. | [optional] 
**name** | **str** | Owner's display name. | [optional] 
**email** | **str** | Owner's email. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.access_apps_owner import AccessAppsOwner

access_apps_owner = AccessAppsOwner(
type='IDENTITY',
id='2c9180a46faadee4016fb4e018c20639',
name='John Doe',
email='john.doe@sailpoint.com'
)

```
[[Back to top]](#) 

