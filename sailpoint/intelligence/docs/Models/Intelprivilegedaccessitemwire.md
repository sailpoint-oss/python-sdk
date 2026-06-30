---
id: intelprivilegedaccessitemwire
title: Intelprivilegedaccessitemwire
pagination_label: Intelprivilegedaccessitemwire
sidebar_label: Intelprivilegedaccessitemwire
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelprivilegedaccessitemwire', 'Intelprivilegedaccessitemwire'] 
slug: /tools/sdk/python/intelligence/models/intelprivilegedaccessitemwire
tags: ['SDK', 'Software Development Kit', 'Intelprivilegedaccessitemwire', 'Intelprivilegedaccessitemwire']
---

# Intelprivilegedaccessitemwire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileged** | **bool** | True when this item is classified as privileged access for the identity. | [required]
**id** | **str** | Identifier of the privileged access item. | [required]
**type** | **str** | Type of privileged access object. | [required]
**display_name** | **str** | Display label for the privileged access item in administrative experiences. | [optional] 
**name** | **str** | Technical name of the privileged access item. | [optional] 
**source** | [**IntelprivilegedaccessitemwireSource**](intelprivilegedaccessitemwire-source) |  | [optional] 
**attribute** | **str** | Source attribute name that carries the privileged value when applicable. | [optional] 
**value** | **str** | Privileged value on the source attribute when applicable. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.intelprivilegedaccessitemwire import Intelprivilegedaccessitemwire

intelprivilegedaccessitemwire = Intelprivilegedaccessitemwire(
privileged=True,
id='ent-1',
type='entitlement',
display_name='Example_Admin_Access',
name='Example_Admin_Access',
source=sailpoint.intelligence.models.intelprivilegedaccessitemwire_source.intelprivilegedaccessitemwire_source(
                    name = 'Example HR Source', 
                    id = 'src-2', ),
attribute='EXAMPLE_PERMISSION_GROUPS',
value='Example_Admin_Access'
)

```
[[Back to top]](#) 

