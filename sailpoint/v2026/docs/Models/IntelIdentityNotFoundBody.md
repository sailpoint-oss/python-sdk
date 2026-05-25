---
id: v2026-intel-identity-not-found-body
title: IntelIdentityNotFoundBody
pagination_label: IntelIdentityNotFoundBody
sidebar_label: IntelIdentityNotFoundBody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityNotFoundBody', 'V2026IntelIdentityNotFoundBody'] 
slug: /tools/sdk/python/v2026/models/intel-identity-not-found-body
tags: ['SDK', 'Software Development Kit', 'IntelIdentityNotFoundBody', 'V2026IntelIdentityNotFoundBody']
---

# IntelIdentityNotFoundBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** |  **Enum** [  'IDC_IDENTITY_NOT_FOUND' ] | Constant detail code indicating that no identity matched the supplied filter. | [required]
**message** | **str** | Optional explanatory text describing why no identity was found. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_identity_not_found_body import IntelIdentityNotFoundBody

intel_identity_not_found_body = IntelIdentityNotFoundBody(
detail_code='IDC_IDENTITY_NOT_FOUND',
message='No identity matched the supplied SCIM filter expression.'
)

```
[[Back to top]](#) 

