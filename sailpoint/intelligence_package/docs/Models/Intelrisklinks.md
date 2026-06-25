---
id: intelrisklinks
title: Intelrisklinks
pagination_label: Intelrisklinks
sidebar_label: Intelrisklinks
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelrisklinks', 'Intelrisklinks'] 
slug: /tools/sdk/python/intelligence-package/models/intelrisklinks
tags: ['SDK', 'Software Development Kit', 'Intelrisklinks', 'Intelrisklinks']
---

# Intelrisklinks

Continuation links for risk responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outliers** | [**Intelhref**](intelhref) | Link to fetch the next outlier page for the same identity. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package.models.intelrisklinks import Intelrisklinks

intelrisklinks = Intelrisklinks(
outliers=sailpoint.intelligence_package.models.intelhref.intelhref(
                    href = '/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/access', )
)

```
[[Back to top]](#) 

