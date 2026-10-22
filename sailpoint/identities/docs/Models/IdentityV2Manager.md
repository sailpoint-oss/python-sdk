---
id: identity-v2-manager
title: IdentityV2Manager
pagination_label: IdentityV2Manager
sidebar_label: IdentityV2Manager
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IdentityV2Manager', 'IdentityV2Manager'] 
slug: /tools/sdk/python/identities/models/identity-v2-manager
tags: ['SDK', 'Software Development Kit', 'IdentityV2Manager', 'IdentityV2Manager']
---

# IdentityV2Manager

The identity's manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the identity's manager. | [optional] 
**name** | **str** | Display name of the identity's manager. | [optional] 
**type** | **str** | DTO type of the identity's manager. | [optional] 
}

## Example

```python
from sailpoint.identities.models.identity_v2_manager import IdentityV2Manager

identity_v2_manager = IdentityV2Manager(
id='2c4180a46faadee4016fb4e018c20626',
name='Robert Robinson',
type='IDENTITY'
)

```
[[Back to top]](#) 

