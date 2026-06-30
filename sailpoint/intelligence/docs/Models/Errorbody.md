---
id: errorbody
title: Errorbody
pagination_label: Errorbody
sidebar_label: Errorbody
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Errorbody', 'Errorbody'] 
slug: /tools/sdk/python/intelligence/models/errorbody
tags: ['SDK', 'Software Development Kit', 'Errorbody', 'Errorbody']
---

# Errorbody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_code** | **str** | Machine-readable error code returned by the Intelligence service. | [optional] 
**message** | **str** | Human-readable explanation of the error suitable for client logging. | [optional] 
}

## Example

```python
from sailpoint.intelligence.models.errorbody import Errorbody

errorbody = Errorbody(
detail_code='IDC_BAD_REQUEST',
message='The filters query parameter is required and cannot be empty.'
)

```
[[Back to top]](#) 

