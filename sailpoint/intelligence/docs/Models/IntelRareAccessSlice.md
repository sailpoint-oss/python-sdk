---
id: intel-rare-access-slice
title: IntelRareAccessSlice
pagination_label: IntelRareAccessSlice
sidebar_label: IntelRareAccessSlice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelRareAccessSlice', 'IntelRareAccessSlice'] 
slug: /tools/sdk/python/intelligence/models/intel-rare-access-slice
tags: ['SDK', 'Software Development Kit', 'IntelRareAccessSlice', 'IntelRareAccessSlice']
---

# IntelRareAccessSlice

Rare access slice embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]IntelOutlierAccessItem**](intel-outlier-access-item) | First page of rare access items for the identity. | [required]
**next** | **str** | Absolute URL to the next rareAccess page; present only when more results exist. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intel_rare_access_slice import IntelRareAccessSlice

intel_rare_access_slice = IntelRareAccessSlice(
items=[
                    sailpoint.intelligence.models.intel_outlier_access_item.IntelOutlierAccessItem(
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

