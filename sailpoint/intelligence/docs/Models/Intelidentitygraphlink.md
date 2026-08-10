---
id: intelidentitygraphlink
title: Intelidentitygraphlink
pagination_label: Intelidentitygraphlink
sidebar_label: Intelidentitygraphlink
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentitygraphlink', 'Intelidentitygraphlink'] 
slug: /tools/sdk/python/intelligence/models/intelidentitygraphlink
tags: ['SDK', 'Software Development Kit', 'Intelidentitygraphlink', 'Intelidentitygraphlink']
---

# Intelidentitygraphlink

Deep link into Identity Graph UI for the resolved identity at the aggregate root. Omitted when the tenant lacks the idg:base license. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Absolute URL to the Identity Graph view. Omitted when the tenant lacks idg:base or when the IDN UI host cannot be resolved from sp-tenant. Query parameters include entity and id for the resolved identity.  | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelidentitygraphlink import Intelidentitygraphlink

intelidentitygraphlink = Intelidentitygraphlink(
href='https://tenant.example.api.cloud.sailpoint.com/ui/identity-graph?entity=identity&id=ef38f94347e94562b5bb8424a56397d8'
)

```
[[Back to top]](#) 

