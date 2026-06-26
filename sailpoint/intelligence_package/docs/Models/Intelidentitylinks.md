---
id: intelidentitylinks
title: Intelidentitylinks
pagination_label: Intelidentitylinks
sidebar_label: Intelidentitylinks
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentitylinks', 'Intelidentitylinks'] 
slug: /tools/sdk/python/intelligence-package/models/intelidentitylinks
tags: ['SDK', 'Software Development Kit', 'Intelidentitylinks', 'Intelidentitylinks']
---

# Intelidentitylinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**Intelhref**](intelhref) | Hyperlink to the Intelligence Package access document for this identity. | [required]
**risk** | [**Intelhref**](intelhref) | Hyperlink to the Intelligence Package risk document for this identity. | [required]
**access_history** | [**Intelhref**](intelhref) | Hyperlink to the Intelligence Package access history document for this identity. | [required]
}

## Example

```python
from sailpoint.intelligence_package.models.intelidentitylinks import Intelidentitylinks

intelidentitylinks = Intelidentitylinks(
access=sailpoint.intelligence_package.models.intelhref.intelhref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', ),
risk=sailpoint.intelligence_package.models.intelhref.intelhref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', ),
access_history=sailpoint.intelligence_package.models.intelhref.intelhref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', )
)

```
[[Back to top]](#) 

