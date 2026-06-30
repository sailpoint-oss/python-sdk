---
id: intelrareaccessslice
title: Intelrareaccessslice
pagination_label: Intelrareaccessslice
sidebar_label: Intelrareaccessslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelrareaccessslice', 'Intelrareaccessslice'] 
slug: /tools/sdk/python/intelligence/models/intelrareaccessslice
tags: ['SDK', 'Software Development Kit', 'Intelrareaccessslice', 'Intelrareaccessslice']
---

# Intelrareaccessslice

Rare access slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]Inteloutlieraccessitem**](inteloutlieraccessitem) | First page of rare access items for the identity. | [required]
**next** | **str** | Absolute URL to the next rareAccess page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelrareaccessslice import Intelrareaccessslice

intelrareaccessslice = Intelrareaccessslice(
items=[
                    sailpoint.intelligence.models.inteloutlieraccessitem.inteloutlieraccessitem(
                        id = 'outlier-access-001', 
                        display_name = 'Example_Admin_Access', 
                        description = '', 
                        access_type = 'ENTITLEMENT', 
                        source_name = 'Example SaaS Source', 
                        extremely_rare = False, )
                    ],
next='https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/outliers/rare-access?limit=10&offset=10'
)

```
[[Back to top]](#) 

