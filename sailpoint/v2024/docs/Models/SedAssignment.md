---
id: v2024-sed-assignment
title: SedAssignment
pagination_label: SedAssignment
sidebar_label: SedAssignment
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'SedAssignment', 'V2024SedAssignment'] 
slug: /tools/sdk/python/v2024/models/sed-assignment
tags: ['SDK', 'Software Development Kit', 'SedAssignment', 'V2024SedAssignment']
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
from sailpoint.v2024.models.sed_assignment import SedAssignment

sed_assignment = SedAssignment(
assignee=sailpoint.v2024.models.sed_assignee.SedAssignee(
                    type = 'SOURCE_OWNER', 
                    value = '016629d1-1d25-463f-97f3-c6686846650', ),
items=[
                    '016629d1-1d25-463f-97f3-0c6686846650'
                    ]
)

```
[[Back to top]](#) 

