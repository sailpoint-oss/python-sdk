---
id: intel-privileged-access-slice
title: IntelPrivilegedAccessSlice
pagination_label: IntelPrivilegedAccessSlice
sidebar_label: IntelPrivilegedAccessSlice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'IntelPrivilegedAccessSlice', 'IntelPrivilegedAccessSlice'] 
slug: /tools/sdk/python/intelligence/models/intel-privileged-access-slice
tags: ['SDK', 'Software Development Kit', 'IntelPrivilegedAccessSlice', 'IntelPrivilegedAccessSlice']
---

# IntelPrivilegedAccessSlice

Full privileged access result embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]IntelPrivilegedAccessItemWire**](intel-privileged-access-item-wire) | Privileged access items for the identity. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intel_privileged_access_slice import IntelPrivilegedAccessSlice

intel_privileged_access_slice = IntelPrivilegedAccessSlice(
items=[
                    sailpoint.intelligence.models.intel_privileged_access_item_wire.IntelPrivilegedAccessItemWire(
                        privileged = True, 
                        id = 'ent-1', 
                        type = 'entitlement', 
                        display_name = 'Example_Admin_Access', 
                        name = 'Example_Admin_Access', 
                        source = sailpoint.intelligence.models.intel_privileged_access_item_wire_source.IntelPrivilegedAccessItemWire_source(
                            name = 'Example HR Source', 
                            id = 'src-2', ), 
                        attribute = 'EXAMPLE_PERMISSION_GROUPS', 
                        value = 'Example_Admin_Access', )
                    ]
)

```
[[Back to top]](#) 

