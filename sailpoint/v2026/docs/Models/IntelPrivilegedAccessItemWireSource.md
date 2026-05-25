---
id: v2026-intel-privileged-access-item-wire-source
title: IntelPrivilegedAccessItemWireSource
pagination_label: IntelPrivilegedAccessItemWireSource
sidebar_label: IntelPrivilegedAccessItemWireSource
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelPrivilegedAccessItemWireSource', 'V2026IntelPrivilegedAccessItemWireSource'] 
slug: /tools/sdk/python/v2026/models/intel-privileged-access-item-wire-source
tags: ['SDK', 'Software Development Kit', 'IntelPrivilegedAccessItemWireSource', 'V2026IntelPrivilegedAccessItemWireSource']
---

# IntelPrivilegedAccessItemWireSource

Source metadata associated with the privileged access item when present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable source name for the privileged access item. | [optional] 
**id** | **str** | Source identifier for the privileged access item. | [optional] 
}

## Example

```python
from sailpoint.v2026.models.intel_privileged_access_item_wire_source import IntelPrivilegedAccessItemWireSource

intel_privileged_access_item_wire_source = IntelPrivilegedAccessItemWireSource(
name='Workday',
id='src-2'
)

```
[[Back to top]](#) 

