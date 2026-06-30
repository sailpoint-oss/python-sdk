---
id: inteloutliersslice
title: Inteloutliersslice
pagination_label: Inteloutliersslice
sidebar_label: Inteloutliersslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Inteloutliersslice', 'Inteloutliersslice'] 
slug: /tools/sdk/python/intelligence/models/inteloutliersslice
tags: ['SDK', 'Software Development Kit', 'Inteloutliersslice', 'Inteloutliersslice']
---

# Inteloutliersslice

Outlier slices embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rare_access** | [**Intelrareaccessslice**](intelrareaccessslice) | First page of rare access items for the identity. | [required]
}

## Example

```python
from sailpoint.intelligence.models.inteloutliersslice import Inteloutliersslice

inteloutliersslice = Inteloutliersslice(
rare_access=sailpoint.intelligence.models.intelrareaccessslice.intelrareaccessslice(
                    items = [
                        sailpoint.intelligence.models.inteloutlieraccessitem.inteloutlieraccessitem(
                            id = 'outlier-access-001', 
                            display_name = 'Example_Admin_Access', 
                            description = '', 
                            access_type = 'ENTITLEMENT', 
                            source_name = 'Example SaaS Source', 
                            extremely_rare = False, )
                        ], 
                    next = 'https://tenant.example.api.cloud.sailpoint.com/v2026/intelligence/identities/ef38f94347e94562b5bb8424a56397d8/outliers/rare-access?limit=10&offset=10', )
)

```
[[Back to top]](#) 

