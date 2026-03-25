---
id: v2026-sed-assignment
title: SedAssignment
pagination_label: SedAssignment
sidebar_label: SedAssignment
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SedAssignment', 'V2026SedAssignment'] 
slug: /tools/sdk/python/v2026/models/sed-assignment
tags: ['SDK', 'Software Development Kit', 'SedAssignment', 'V2026SedAssignment']
---

# SedAssignment

Sed Assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**SedAssignee**](sed-assignee) |  | [optional] 
**items** | **[]str** | List of SED id's | [optional] 
}

## Example

```python
from sailpoint.v2026.models.sed_assignment import SedAssignment

sed_assignment = SedAssignment(
assignee=sailpoint.v2026.models.sed_assignee.Sed Assignee(
                    type = 'SOURCE_OWNER', 
                    value = '016629d1-1d25-463f-97f3-c6686846650', ),
items=[
                    '016629d1-1d25-463f-97f3-0c6686846650'
                    ]
)

```
[[Back to top]](#) 

