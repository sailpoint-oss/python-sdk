---
id: v2025-authorization-scheme
title: AuthorizationScheme
pagination_label: AuthorizationScheme
sidebar_label: AuthorizationScheme
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'AuthorizationScheme', 'V2025AuthorizationScheme'] 
slug: /tools/sdk/python/v2025/models/authorization-scheme
tags: ['SDK', 'Software Development Kit', 'AuthorizationScheme', 'V2025AuthorizationScheme']
---

# AuthorizationScheme

Authorization scheme supported by the transmitter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_urn** | **str** | URN describing the authorization specification. OAuth 2.0: `urn:ietf:rfc:6749`; Bearer token: `urn:ietf:rfc:6750`.  | [optional] 
}

## Example

```python
from sailpoint.v2025.models.authorization_scheme import AuthorizationScheme

authorization_scheme = AuthorizationScheme(
spec_urn='urn:ietf:rfc:6749'
)

```
[[Back to top]](#) 

