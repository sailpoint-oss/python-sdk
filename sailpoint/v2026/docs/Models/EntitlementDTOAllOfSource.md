---
id: v2026-entitlement-dto-all-of-source
title: EntitlementDTOAllOfSource
pagination_label: EntitlementDTOAllOfSource
sidebar_label: EntitlementDTOAllOfSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'EntitlementDTOAllOfSource', 'V2026EntitlementDTOAllOfSource'] 
slug: /tools/sdk/python/v2026/models/entitlement-dto-all-of-source
tags: ['SDK', 'Software Development Kit', 'EntitlementDTOAllOfSource', 'V2026EntitlementDTOAllOfSource']
---

# EntitlementDTOAllOfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object reference id | [optional] 
**value** | **str** | Object reference name | [optional] 
**type** | **str** | SOURCE (added because exists in Entitlement V3) | [optional] 
}

## Example

```python
from sailpoint.v2026.models.entitlement_dto_all_of_source import EntitlementDTOAllOfSource

entitlement_dto_all_of_source = EntitlementDTOAllOfSource(
id='2b86153b97a94abc936c8a11b106aaf8',
value='accountant',
type='SOURCE'
)

```
[[Back to top]](#) 

