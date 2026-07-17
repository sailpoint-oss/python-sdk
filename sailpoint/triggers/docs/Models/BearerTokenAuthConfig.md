---
id: bearer-token-auth-config
title: BearerTokenAuthConfig
pagination_label: BearerTokenAuthConfig
sidebar_label: BearerTokenAuthConfig
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'BearerTokenAuthConfig', 'BearerTokenAuthConfig'] 
slug: /tools/sdk/python/triggers/models/bearer-token-auth-config
tags: ['SDK', 'Software Development Kit', 'BearerTokenAuthConfig', 'BearerTokenAuthConfig']
---

# BearerTokenAuthConfig

Config required if BEARER_TOKEN authentication is used. On response, this field is set to null as to not return secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer_token** | **str** | Bearer token | [optional] 
}

## Example

```python
from sailpoint.triggers.models.bearer_token_auth_config import BearerTokenAuthConfig

bearer_token_auth_config = BearerTokenAuthConfig(
bearer_token=''
)

```
[[Back to top]](#) 

