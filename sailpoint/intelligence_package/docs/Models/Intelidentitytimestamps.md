---
id: intelidentitytimestamps
title: Intelidentitytimestamps
pagination_label: Intelidentitytimestamps
sidebar_label: Intelidentitytimestamps
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Intelidentitytimestamps', 'Intelidentitytimestamps'] 
slug: /tools/sdk/python/intelligence-package/models/intelidentitytimestamps
tags: ['SDK', 'Software Development Kit', 'Intelidentitytimestamps', 'Intelidentitytimestamps']
---

# Intelidentitytimestamps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the identity record was first created in Identity Security Cloud. | [required]
**modified_at** | **datetime** | Timestamp when the identity record was last modified in Identity Security Cloud. | [required]
}

## Example

```python
from sailpoint.intelligence_package.models.intelidentitytimestamps import Intelidentitytimestamps

intelidentitytimestamps = Intelidentitytimestamps(
created_at='2024-01-15T10:30Z',
modified_at='2024-06-20T14:45Z'
)

```
[[Back to top]](#) 

