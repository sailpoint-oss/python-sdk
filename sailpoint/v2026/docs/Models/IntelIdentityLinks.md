---
id: v2026-intel-identity-links
title: IntelIdentityLinks
pagination_label: IntelIdentityLinks
sidebar_label: IntelIdentityLinks
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelIdentityLinks', 'V2026IntelIdentityLinks'] 
slug: /tools/sdk/python/v2026/models/intel-identity-links
tags: ['SDK', 'Software Development Kit', 'IntelIdentityLinks', 'V2026IntelIdentityLinks']
---

# IntelIdentityLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**IntelHref**](intel-href) | Hyperlink to the Intelligence Package access document for this identity. | [required]
**access_history** | [**IntelHref**](intel-href) | Hyperlink to the Intelligence Package access history document for this identity. | [required]
}

## Example

```python
from sailpoint.v2026.models.intel_identity_links import IntelIdentityLinks

intel_identity_links = IntelIdentityLinks(
access=sailpoint.v2026.models.intel_href.IntelHref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', ),
access_history=sailpoint.v2026.models.intel_href.IntelHref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', )
)

```
[[Back to top]](#) 

