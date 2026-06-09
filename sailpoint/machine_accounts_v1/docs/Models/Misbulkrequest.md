---
id: misbulkrequest
title: Misbulkrequest
pagination_label: Misbulkrequest
sidebar_label: Misbulkrequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Misbulkrequest', 'Misbulkrequest'] 
slug: /tools/sdk/python/v1/models/misbulkrequest
tags: ['SDK', 'Software Development Kit', 'Misbulkrequest', 'Misbulkrequest']
---

# Misbulkrequest

Request body listing machine identity or machine account IDs for a bulk operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | Machine identity or machine account IDs to include in the bulk operation. | [required]
}

## Example

```python
from sailpoint.machine_accounts_v1.models.misbulkrequest import Misbulkrequest

misbulkrequest = Misbulkrequest(
ids=["ef38f94347e94562b5bb8424a56397d8","2c91808a7813090a017814121919ecca"]
)

```
[[Back to top]](#) 

