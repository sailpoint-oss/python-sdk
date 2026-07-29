---
id: intelprivilegelevel
title: Intelprivilegelevel
pagination_label: Intelprivilegelevel
sidebar_label: Intelprivilegelevel
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelprivilegelevel', 'Intelprivilegelevel'] 
slug: /tools/sdk/python/intelligence/models/intelprivilegelevel
tags: ['SDK', 'Software Development Kit', 'Intelprivilegelevel', 'Intelprivilegelevel']
---

# Intelprivilegelevel

Effective privilege level for the privileged access item. Set to HIGH, MEDIUM, or LOW based on the tenant's privilege classification configuration, including connector criteria, custom criteria, manual overrides, or a single configured privilege level. Use NONE when no privilege level is assigned. Entitlements previously marked with privileged=true are classified as HIGH. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective** |  **Enum** [  'HIGH',    'MEDIUM',    'LOW',    'NONE' ] | Effective privilege level for the privileged access item.  | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelprivilegelevel import Intelprivilegelevel

intelprivilegelevel = Intelprivilegelevel(
effective='HIGH'
)

```
[[Back to top]](#) 

