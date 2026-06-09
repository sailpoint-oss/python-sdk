---
id: intelprivilegedaccessitemwire
title: Intelprivilegedaccessitemwire
pagination_label: Intelprivilegedaccessitemwire
sidebar_label: Intelprivilegedaccessitemwire
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelprivilegedaccessitemwire', 'Intelprivilegedaccessitemwire'] 
slug: /tools/sdk/python/v1/models/intelprivilegedaccessitemwire
tags: ['SDK', 'Software Development Kit', 'Intelprivilegedaccessitemwire', 'Intelprivilegedaccessitemwire']
---

# Intelprivilegedaccessitemwire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileged** | **bool** | True when SDS Search classifies this item as privileged access for the identity. | [required]
**display_name** | **str** | Display label for the privileged access item in administrative experiences. | [optional] 
**name** | **str** | Technical name of the privileged access item from SDS Search. | [optional] 
**standalone** | **bool** | True when the privileged item is modeled as a standalone entitlement or access object. | [optional] [default to False]
**id** | **str** | Identifier of the privileged access item returned by SDS Search. | [required]
**source** | [**IntelprivilegedaccessitemwireSource**](intelprivilegedaccessitemwire-source) |  | [optional] 
**attribute** | **str** | Source attribute name that carries the privileged value when applicable. | [optional] 
**type** | **str** | Object type classification from SDS Search (for example ENTITLEMENT). | [required]
**value** | **str** | Privileged value on the source attribute when applicable. | [optional] 
}

## Example

```python
from sailpoint.intelligence_package_v1.models.intelprivilegedaccessitemwire import Intelprivilegedaccessitemwire

intelprivilegedaccessitemwire = Intelprivilegedaccessitemwire(
privileged=True,
display_name='Absence_Administrator',
name='Absence_Administrator',
standalone=True,
id='ent-1',
source=sailpoint.intelligence_package_v1.models.intelprivilegedaccessitemwire_source.intelprivilegedaccessitemwire_source(
                    name = 'Workday', 
                    id = 'src-2', ),
attribute='USER_BASED_SECURITY_GROUPS',
type='ENTITLEMENT',
value='Absence_Administrator'
)

```
[[Back to top]](#) 

