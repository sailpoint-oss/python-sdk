---
id: v2026-intel-privileged-access-item-wire
title: IntelPrivilegedAccessItemWire
pagination_label: IntelPrivilegedAccessItemWire
sidebar_label: IntelPrivilegedAccessItemWire
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelPrivilegedAccessItemWire', 'V2026IntelPrivilegedAccessItemWire'] 
slug: /tools/sdk/python/v2026/models/intel-privileged-access-item-wire
tags: ['SDK', 'Software Development Kit', 'IntelPrivilegedAccessItemWire', 'V2026IntelPrivilegedAccessItemWire']
---

# IntelPrivilegedAccessItemWire


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileged** | **bool** | True when SDS Search classifies this item as privileged access for the identity. | [required]
**display_name** | **str** | Display label for the privileged access item in administrative experiences. | [optional] 
**name** | **str** | Technical name of the privileged access item from SDS Search. | [optional] 
**standalone** | **bool** | True when the privileged item is modeled as a standalone entitlement or access object. | [optional] [default to False]
**id** | **str** | Identifier of the privileged access item returned by SDS Search. | [required]
**source** | [**IntelPrivilegedAccessItemWireSource**](intel-privileged-access-item-wire-source) |  | [optional] 
**attribute** | **str** | Source attribute name that carries the privileged value when applicable. | [optional] 
**type** | **str** | Object type classification from SDS Search (for example ENTITLEMENT). | [required]
**value** | **str** | Privileged value on the source attribute when applicable. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_privileged_access_item_wire import IntelPrivilegedAccessItemWire

intel_privileged_access_item_wire = IntelPrivilegedAccessItemWire(
privileged=True,
display_name='Example_Admin_Access',
name='Example_Admin_Access',
standalone=True,
id='ent-1',
source=sailpoint.v2026.models.intel_privileged_access_item_wire_source.IntelPrivilegedAccessItemWire_source(
                    name = 'Example HR Source', 
                    id = 'src-2', ),
attribute='EXAMPLE_PERMISSION_GROUPS',
type='ENTITLEMENT',
value='Example_Admin_Access'
)

```
[[Back to top]](#) 

