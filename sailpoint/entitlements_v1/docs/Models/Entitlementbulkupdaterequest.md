---
id: entitlementbulkupdaterequest
title: Entitlementbulkupdaterequest
pagination_label: Entitlementbulkupdaterequest
sidebar_label: Entitlementbulkupdaterequest
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'Entitlementbulkupdaterequest', 'Entitlementbulkupdaterequest'] 
slug: /tools/sdk/python/v1/models/entitlementbulkupdaterequest
tags: ['SDK', 'Software Development Kit', 'Entitlementbulkupdaterequest', 'Entitlementbulkupdaterequest']
---

# Entitlementbulkupdaterequest

Object for specifying the bulk update request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_ids** | **[]str** | List of entitlement ids to update | [required]
**json_patch** | [**[]Jsonpatchoperation**](jsonpatchoperation) |  | [required]
}

## Example

```python
from sailpoint.entitlements_v1.models.entitlementbulkupdaterequest import Entitlementbulkupdaterequest

entitlementbulkupdaterequest = Entitlementbulkupdaterequest(
entitlement_ids=["2c91808a7624751a01762f19d665220d","2c91808a7624751a01762f19d67c220e","2c91808a7624751a01762f19d692220f"],
json_patch=[{"op":"replace","path":"/requestable","value":false},{"op":"replace","path":"/privilegeOverride/level","value":"HIGH"}]
)

```
[[Back to top]](#) 

