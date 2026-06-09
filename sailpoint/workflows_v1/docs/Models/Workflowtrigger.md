---
id: workflowtrigger
title: Workflowtrigger
pagination_label: Workflowtrigger
sidebar_label: Workflowtrigger
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Workflowtrigger', 'Workflowtrigger'] 
slug: /tools/sdk/python/v1/models/workflowtrigger
tags: ['SDK', 'Software Development Kit', 'Workflowtrigger', 'Workflowtrigger']
---

# Workflowtrigger

The trigger that starts the workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** |  **Enum** [  'EVENT',    'EXTERNAL',    'SCHEDULED',    '' ] | The trigger type | [required]
**display_name** | **str** | The trigger display name | [optional] 
**attributes** | **object** | Workflow Trigger Attributes. | [required]
}

## Example

```python
from sailpoint.workflows_v1.models.workflowtrigger import Workflowtrigger

workflowtrigger = Workflowtrigger(
type='EVENT',
display_name='',
attributes=None
)

```
[[Back to top]](#) 

