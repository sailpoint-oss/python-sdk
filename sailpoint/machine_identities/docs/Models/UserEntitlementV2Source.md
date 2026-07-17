---
id: user-entitlement-v2-source
title: UserEntitlementV2Source
pagination_label: UserEntitlementV2Source
sidebar_label: UserEntitlementV2Source
sidebar_class_name: pythonsdk
keywords: ['python', 'Python', 'sdk', 'UserEntitlementV2Source', 'UserEntitlementV2Source'] 
slug: /tools/sdk/python/machine-identities/models/user-entitlement-v2-source
tags: ['SDK', 'Software Development Kit', 'UserEntitlementV2Source', 'UserEntitlementV2Source']
---

# UserEntitlementV2Source

The source of the entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **DtoType** |  | [optional] 
**id** | **str** | ID of the object to which this reference applies | [optional] 
**name** | **str** | Human-readable display name of the object to which this reference applies | [optional] 
}

## Example

```python
from sailpoint.machine_identities.models.user_entitlement_v2_source import UserEntitlementV2Source

user_entitlement_v2_source = UserEntitlementV2Source(
type='IDENTITY',
id='2c91808568c529c60168cca6f90c1313',
name='William Wilson'
)

```
[[Back to top]](#) 

