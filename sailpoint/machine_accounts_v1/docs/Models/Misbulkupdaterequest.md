---
id: misbulkupdaterequest
title: Misbulkupdaterequest
pagination_label: Misbulkupdaterequest
sidebar_label: Misbulkupdaterequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Misbulkupdaterequest', 'Misbulkupdaterequest'] 
slug: /tools/sdk/python/v1/models/misbulkupdaterequest
tags: ['SDK', 'Software Development Kit', 'Misbulkupdaterequest', 'Misbulkupdaterequest']
---

# Misbulkupdaterequest

Request body for applying the same JSON Patch document to multiple machine identities or machine accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **[]str** | Machine identity or machine account IDs to update. | [required]
**json_patch** | [**[]Jsonpatchoperation**](jsonpatchoperation) | JSON Patch operations to apply to each ID in the request (RFC 6902). | [required]
}

## Example

```python
from sailpoint.machine_accounts_v1.models.misbulkupdaterequest import Misbulkupdaterequest

misbulkupdaterequest = Misbulkupdaterequest(
ids=["ef38f94347e94562b5bb8424a56397d8"],
json_patch=[{"op":"replace","path":"/description","value":"Updated description"}]
)

```
[[Back to top]](#) 

