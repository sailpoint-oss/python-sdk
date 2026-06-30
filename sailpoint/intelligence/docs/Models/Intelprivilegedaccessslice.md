---
id: intelprivilegedaccessslice
title: Intelprivilegedaccessslice
pagination_label: Intelprivilegedaccessslice
sidebar_label: Intelprivilegedaccessslice
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelprivilegedaccessslice', 'Intelprivilegedaccessslice'] 
slug: /tools/sdk/python/intelligence/models/intelprivilegedaccessslice
tags: ['SDK', 'Software Development Kit', 'Intelprivilegedaccessslice', 'Intelprivilegedaccessslice']
---

# Intelprivilegedaccessslice

Full privileged access result embedded in the aggregate identity response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[]Intelprivilegedaccessitemwire**](intelprivilegedaccessitemwire) | Privileged access items for the identity. | [required]
}

## Example

```python
from sailpoint.intelligence.models.intelprivilegedaccessslice import Intelprivilegedaccessslice

intelprivilegedaccessslice = Intelprivilegedaccessslice(
items=[
                    sailpoint.intelligence.models.intelprivilegedaccessitemwire.intelprivilegedaccessitemwire(
                        privileged = True, 
                        id = 'ent-1', 
                        type = 'entitlement', 
                        display_name = 'Example_Admin_Access', 
                        name = 'Example_Admin_Access', 
                        source = sailpoint.intelligence.models.intelprivilegedaccessitemwire_source.intelprivilegedaccessitemwire_source(
                            name = 'Example HR Source', 
                            id = 'src-2', ), 
                        attribute = 'EXAMPLE_PERMISSION_GROUPS', 
                        value = 'Example_Admin_Access', )
                    ]
)

```
[[Back to top]](#) 

